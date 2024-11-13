from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import OPERATOR
from data.translate import msg_lang
from loader import dp, db, bot
from states.shopping import Shopping
from keyboards.default.cancel import cancel_btn
from keyboards.default.main_menu import get_main_btn


@dp.message_handler(lambda msg: "🛍 Shopping" in msg.text)
async def leave_comment(msg: types.Message):
    lang = (db.select_user(tg_id=msg.from_user.id))[3]
    msg_txt = msg_lang["shopping_link"][lang]
    btn = cancel_btn(lang)
    await msg.answer(msg_txt, reply_markup=btn)
    await Shopping.first()


@dp.message_handler(state=Shopping.link)
async def leave_comment(msg: types.Message, state: FSMContext):
    lang = db.select_user(tg_id=msg.from_user.id)
    btn = get_main_btn(lang[3])
    if msg.text in ("Отмена", "Bekor qilish"):
        txt = msg_lang["main_menu"][lang[3]]
        await msg.answer(txt, reply_markup=btn)
        await state.finish()
        return
    btn = cancel_btn(lang[3])
    msg_txt = msg_lang["shopping_image"][lang[3]]
    await msg.answer(msg_txt, reply_markup=btn)
    await state.update_data(link=msg.text)
    await Shopping.next()


@dp.message_handler(state=Shopping.image, content_types=types.ContentType.PHOTO)
async def leave_comment(msg: types.Message, state: FSMContext):
    lang = db.select_user(tg_id=msg.from_user.id)
    data = await state.get_data()
    await state.finish()
    link = data['link']
    photo = msg.photo[-1]['file_id']
    txt = msg_lang["shopping_end"][lang[3]]
    await msg.answer(txt, reply_markup=get_main_btn(lang[3]))
    msg_txt = f"<b>ID kod:</b> {lang[7]}\n<b>Ismi:</b> {lang[1]}\n<b>Telefon raqami:</b> {lang[2]}\n\n<b>Tovar havolasi:</b> {link}"
    await bot.send_photo(OPERATOR, photo, msg_txt)


@dp.message_handler(state=Shopping.image)
async def leave_comment(msg: types.Message, state: FSMContext):
    lang = db.select_user(tg_id=msg.from_user.id)
    btn = get_main_btn(lang[3])
    if msg.text in ("Отмена", "Bekor qilish"):
        txt = msg_lang["main_menu"][lang[3]]
        await msg.answer(txt, reply_markup=btn)
        await state.finish()
        return
    btn = cancel_btn(lang[3])
    txt = msg_lang["shopping_image_err"][lang[3]]
    await msg.answer(txt, reply_markup=btn)
