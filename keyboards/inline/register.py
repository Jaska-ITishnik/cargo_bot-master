from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.translate import btn_lang


def register_btn(lang):
    res = InlineKeyboardMarkup(row_width=2)
    res.insert(InlineKeyboardButton(btn_lang['register'][lang], callback_data='auth_register'))
    res.insert(InlineKeyboardButton(btn_lang['login'][lang], callback_data='auth_login'))
    return res


def phone_number2(lang):
    res = InlineKeyboardMarkup(row_width=2)
    res.insert(InlineKeyboardButton(btn_lang['phone_number2_yes'][lang], callback_data='phone2_yes'))
    res.insert(InlineKeyboardButton(btn_lang['phone_number2_no'][lang], callback_data='phone2_no'))
    return res
