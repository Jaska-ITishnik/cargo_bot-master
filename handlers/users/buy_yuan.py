from aiogram import types

from data.translate import msg_lang
from keyboards.inline.choose_lang import buy_yuan
from loader import dp, db


@dp.message_handler(lambda message: '💳' in message.text)
async def trek_code(message: types.Message):
    lang = (db.select_user(tg_id=message.from_user.id))[3]
    msg = msg_lang['buy_yuan'][lang]
    await message.answer(msg, reply_markup=buy_yuan(lang))
