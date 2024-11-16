from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from magic_filter import F

from data.translate import manzils, btn_lang, msg_lang
from loader import dp, db


@dp.message_handler(lambda message: "🎫" in message.text)
async def get_address(message: types.Message):
    user = db.select_user(tg_id=message.from_user.id)
    print(user)
    ikb = InlineKeyboardMarkup()
    ikb.row(
        InlineKeyboardButton(text=btn_lang['address_type']['avto'][user['lang']], callback_data='_AVTO🚛'),
        InlineKeyboardButton(text=btn_lang['address_type']['avia'][user['lang']], callback_data='_AVIA✈')
    )
    buttons = ikb
    await message.answer(msg_lang['address_description'][user['lang']], reply_markup=buttons)

@dp.callback_query_handler((F.data == '_AVIA✈') | (F.data == '_AVTO🚛'))
async def check_address(callback: CallbackQuery):
    user = db.select_user(tg_id=callback.from_user.id)
    id_code = user['id_code']
    if callback.data == '_AVIA✈':
        await callback.message.delete()
        await callback.message.answer(manzils['avia'][user['lang']].format(code=id_code))
    else:
        await callback.message.delete()
        await callback.message.answer(manzils['avto'][user['lang']].format(code=id_code))
