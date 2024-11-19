from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, ContentType
from environs import Env

from data.config import OPERATOR, ADMINS
from data.translate import msg_lang
from keyboards.default.cancel import cancel_btn
from keyboards.default.deliver import deliver_or_not
from keyboards.default.main_menu import get_main_btn
from keyboards.default.register_btn import send_location
from loader import dp, db, bot
from states.send_message_admin import AdminSendMessage
from states.trek_code import Trek_code

env = Env()
env.read_env()


@dp.message_handler(
    lambda x: x.text in ("🔎 Проверка трек-кода", "🔎 Trek kodini tekshirish")
)
async def trek_code(msg: types.Message):
    lang = db.select_user(tg_id=msg.from_user.id)
    trek_code = db.select_product_trek_code(user_id=lang['id'])
    print(trek_code)
    txt = msg_lang["trek_code"][lang['lang']]
    btn = cancel_btn(lang['lang'])
    await msg.answer(txt, reply_markup=btn)
    await Trek_code.first()


@dp.message_handler(lambda x: x.text in ("↩ Войти в админку", "↩ Adminkaga kirish"))
async def admin_panel(msg: types.Message):
    # Create an inline keyboard with a Web App URL button
    ikb = InlineKeyboardMarkup()
    button = InlineKeyboardButton('ADMINKA', url="http://217.77.4.131:8008/admin/")
    await msg.answer('👇', reply_markup=ikb.add(button))
    await msg.delete()


@dp.message_handler(lambda x: x.text in ("📨 Xabar yuborish", "📨 Отправить сообщение"))
async def admin_send_message(msg: Message, state: FSMContext):
    if str(msg.from_user.id) in ADMINS:
        await state.set_state(AdminSendMessage.message)
        await msg.answer(f"{msg.from_user.first_name} xabarni yuborishingiz mumkin")
    else:
        await msg.answer("Kechirasiz xabarni faqat adminlar yuboraoladi🤙")


@dp.message_handler(content_types=[ContentType.TEXT, ContentType.PHOTO, ContentType.VIDEO],
                    state=AdminSendMessage.message)
async def admin_send_message_state(msg: Message, state: FSMContext):
    await state.update_data(message=msg.text)
    data = await state.get_data()
    users = db.select_all_users()
    for user in users:
        if str(user['tg_id']) not in ADMINS:
            if msg.photo:
                await msg.bot.send_photo(chat_id=user['tg_id'], photo=msg.photo[0].file_id, caption=msg.caption)
            if msg.video:
                await msg.bot.send_video(chat_id=user['tg_id'], video=msg.video.file_id, caption=msg.caption)
            else:
                if data.get('message'):
                    await msg.bot.send_message(chat_id=user['tg_id'], text=data['message'])
    await msg.answer("Yana xabar yuborish qayta /start qilib xabar yuboring")


@dp.message_handler(state=Trek_code.code)
async def code_ans(msg: types.Message, state=FSMContext):
    lang = db.select_user(tg_id=msg.from_user.id)
    if msg.text in ("Отмена", "Bekor qilish"):
        txt = msg_lang["main_menu"][lang['lang']]
        btn = get_main_btn(lang['lang'], msg)
        await msg.answer(txt, reply_markup=btn)
        await state.finish()
        return
    all_trek_codes_from_db = db.select_product_trek_code(user_id=lang['id'])[0]['trek_code']
    trek_codes_list = [i[0] for i in all_trek_codes_from_db]
    if msg.text in all_trek_codes_from_db:
        is_arrived_or_is_taken = db.select_product_arrive_taken(trek_code=msg.text)
        if (is_arrived_or_is_taken[0]['is_arrived'] and is_arrived_or_is_taken[0]['is_taken']) and True:
            txt = msg_lang["taken"][lang['lang']]
            btn = get_main_btn(lang['lang'], msg)
            await msg.answer(txt, reply_markup=btn)
            await state.finish()
        elif is_arrived_or_is_taken[0]['is_arrived']:
            txt = msg_lang["deliver_or_not"][lang['lang']]
            btn = deliver_or_not(lang['lang'])
            await msg.answer(txt, reply_markup=btn)
            await Trek_code.next()
        else:
            txt = msg_lang["not_arrived"][lang['lang']]
            btn = get_main_btn(lang['lang'], msg)
            await msg.answer(txt, reply_markup=btn)
            await state.finish()
    else:
        txt = msg_lang["no_trek_code"][lang['lang']]
        btn = cancel_btn(lang['lang'])
        await msg.answer(txt, reply_markup=btn)
        return


@dp.message_handler(state=Trek_code.deliver_type)
async def deliver_type_ans(msg: types.Message, state=FSMContext):
    lang = db.select_user(tg_id=msg.from_user.id)
    if msg.text in ("Забрать самому", "Borib olish"):
        txt = msg_lang["bring_deliver"][lang['lang']]
        btn = get_main_btn(lang['lang'], msg)
        await bot.send_location(
            chat_id=msg.chat.id,
            latitude=env.str("LATITUDE"),
            longitude=env.str("LONGITUDE"),
        )
        await msg.answer(txt, reply_markup=btn)
        await state.finish()
    elif msg.text in (
            "Сделать доставку",
            "Buyurtmani yuborish(dostavka)",
    ):
        txt = msg_lang["deliver"][lang['lang']]
        btn = send_location(lang['lang'])
        await msg.answer(txt, reply_markup=btn)
        await Trek_code.next()
    else:
        return


@dp.message_handler(
    content_types=(types.ContentType.LOCATION, types.ContentType.TEXT),
    state=Trek_code.get_location,
)
async def get_loc_ans(msg: types.Message, state=FSMContext):
    lang = db.select_user(tg_id=msg.from_user.id)
    if msg.text:
        txt = msg_lang["not_address"][lang['lang']]
        btn = send_location(lang['lang'])
        await msg.answer(txt, reply_markup=btn)
        return
    else:
        latitude = msg.location.latitude
        longitude = msg.location.longitude
        print(latitude, longitude)
        db.update_user_loc(latitude, longitude, msg.from_user.id)
        txt = msg_lang["success_deliver"][lang['lang']]
        btn = get_main_btn(lang['lang'], msg)
        await msg.answer(txt, reply_markup=btn)
        await state.finish()
        await bot.send_location(OPERATOR, latitude=latitude, longitude=longitude)
        await bot.send_message(
            chat_id=OPERATOR,
            text=f"New location to delivery❗️\nUsername:{msg.from_user.username}\nPhone:{lang['phone_number']}, {lang[11]}",
        )
