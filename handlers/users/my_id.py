from aiogram import types

from data.translate import msg_lang
from loader import dp, db


@dp.message_handler(lambda msg: "ID" in msg.text)
async def my_id_handler(msg: types.Message):
    user = db.select_user(tg_id=msg.from_user.id)
    lang = user['lang']
    msg_txt = msg_lang['select_myid'][lang].format(user['id_code'])
    await msg.answer(msg_txt)
