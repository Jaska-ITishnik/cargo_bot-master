from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from data.translate import msg_lang
from keyboards.default.main_menu import get_main_btn
from keyboards.inline.choose_lang import langs
from keyboards.inline.register import register_btn
from loader import dp, db
from states.register import ChooseLang


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    if len(message.text) > 6:
        referal_person = message.text[7:]
        db.update_referal(referal_person, 1)
        referal_id = db.get_referal(referal_person)[0]
        db.create_user_referal(message.from_user.id, referal_id)

    msg = (
        f"Assalomu aleykum, {message.from_user.full_name}! FAD Cargo - Xitoydan yetkazib berish xizmatining rasmiy botiga xush kelibsiz!\n\n"
        f"•~•~•~•~•~•~•~•~•~\n\n"
        f"Привет,  ! Добро пожаловать в официальный бот FAD Cargo - Доставка из Китая!")

    users = [user['tg_id'] for user in db.selects_users(is_active=True)]
    if message.from_user.id in users:
        user_lang = (db.select_user(tg_id=message.from_user.id))['lang']
        await message.answer(msg_lang['greeting'][user_lang].format(message.from_user.first_name),
                             reply_markup=get_main_btn(user_lang, message))
    else:
        msg += "\n\n🇺🇿 Tilni tanlang\n🇷🇺 Выберите язык"
        await message.answer(msg, reply_markup=langs)


@dp.callback_query_handler(lambda c: c.data.startswith('lang'))
async def choose_l(call: types.CallbackQuery, state: FSMContext):
    lang = call.data.split('_')[1]
    await state.update_data(lang=lang)
    msg = msg_lang['auth'][lang]
    btn = register_btn(lang)
    await ChooseLang.first()
    await call.message.edit_text(msg, reply_markup=btn)
