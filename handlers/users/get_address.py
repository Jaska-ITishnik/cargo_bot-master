from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from magic_filter import F

from data.translate import manzils, btn_lang, msg_lang
from loader import dp, db
from utils.db_api.sqlite import Database


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
    address_options = list(Database().select_address_options())[0]
    period_avia = address_options['period_avia']
    period_avto = address_options['period_avto']
    phone_number = address_options['phone_number']
    mail_address = address_options['mail_address']
    address = address_options['address']
    user = db.select_user(tg_id=callback.from_user.id)
    id_code = user['id_code']
    if callback.data == '_AVIA✈':
        await callback.message.delete()
        await callback.message.answer(
            manzils['avia'][user['lang']].format(code=id_code, period_avia=period_avia, phone_number=phone_number,
                                                 mail_address=mail_address, address=address))
    else:
        await callback.message.delete()
        await callback.message.answer(
            manzils['avto'][user['lang']].format(code=id_code, period_avto=period_avto, phone_number=phone_number,
                                                 mail_address=mail_address, address=address))
