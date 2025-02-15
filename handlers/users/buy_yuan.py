from aiogram import types

from data.config import YUAN_BOT
from data.translate import msg_lang
from loader import dp, db


@dp.message_handler(lambda message: '💳' in message.text)
async def trek_code(message: types.Message):
    lang = (db.select_user(tg_id=message.from_user.id))['lang']
    msg = msg_lang['buy_yuan'][lang]
    await message.answer("👇")
    await message.answer(text=f"➡: {YUAN_BOT}")
