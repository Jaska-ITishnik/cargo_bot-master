from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from data.translate import btn_lang


def send_phone(lang):
    res = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    res.add(KeyboardButton(btn_lang['send_phone'][lang], request_contact=True))
    return res


def send_location(lang):
    res = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    res.add(KeyboardButton(btn_lang['send_location'][lang], request_location=True))
    return res


def choose_manzil(lang, id_code):
    res = InlineKeyboardMarkup(resize_keyboard=True)
    res.add(InlineKeyboardButton(btn_lang['choose_manzil'][lang], callback_data=f'manzil_{id_code}'))
    return res
