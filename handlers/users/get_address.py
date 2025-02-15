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
    user = db.select_user(tg_id=callback.from_user.id)
    id_code = user['id_code']
    address_options = list(Database().select_address_options())
    avia_address_msg = ''
    avto_address_msg = ''
    for address_option in address_options:
        period_avia = address_option['period_avia']
        period_avto = address_option['period_avto']
        phone_number = address_option['phone_number']
        mail_address = address_option['mail_address']
        address = address_option['address']
        avia_address_msg += f"""{manzils['avia'][user['lang']].format(code=id_code, period_avia=period_avia,
                                                                      phone_number=phone_number,
                                                                      mail_address=mail_address, address=address)}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
        avto_address_msg += f"""{manzils['avto'][user['lang']].format(code=id_code, period_avto=period_avto,
                                                                      phone_number=phone_number,
                                                                      mail_address=mail_address, address=address)}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
    if callback.data == '_AVIA✈':
        await callback.message.delete()
        await callback.message.answer(text=avia_address_msg)
    else:
        await callback.message.delete()
        await callback.message.answer(text=avto_address_msg)
