from aiogram import types

from data.translate import manzils
from loader import dp, db


@dp.message_handler(lambda message: "🎫" in message.text)
async def get_address(message: types.Message):
    user = db.select_user(tg_id=message.from_user.id)
    print(user)
    id_code = user[9]
    # d = {
    #     'A': 0,
    #     'B': 1,
    #     'C': 2
    # }
    for i in list(manzils.values()):
        await message.answer(i[user[4]].format(code=id_code))

