from aiogram import types
from aiogram.dispatcher import FSMContext

from data.translate import msg_lang
from keyboards.default.main_menu import get_main_btn
from loader import dp, db
from states.register import Login
from utils.own_funcs import valid_phone

login_msg = msg_lang['login']


@dp.message_handler(state=Login.phone_number)
async def register_phone_number(msg: types.Message, state: FSMContext):
    lang = (await state.get_data())['lang']
    valid = valid_phone(msg.text, lang)
    if valid != msg.text:
        await msg.answer(valid)
        return
    users = db.selects_users(phone_number=msg.text[1:])
    if users:
        await state.update_data(phone_number=msg.text[1:])
        await msg.answer(login_msg['id_code'][lang])
        await Login.next()
    else:
        await msg.answer(login_msg['error_phone'][lang])
        await state.finish()


@dp.message_handler(state=Login.id_code)
async def register_phone_number(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    users = db.selects_users(phone_number=data['phone_number'], id_code=msg.text)
    lang = (await state.get_data())['lang']
    if users:
        db.update_user(data['phone_number'], is_active=True, tg_id=msg.from_user.id)
        await msg.answer(msg_lang['greeting'][lang].format(msg.from_user.first_name), reply_markup=get_main_btn(lang))
    else:
        await msg.answer(login_msg['error_idcode'][lang])
    await state.finish()
