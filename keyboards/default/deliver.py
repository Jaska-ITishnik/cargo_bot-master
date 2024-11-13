from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.translate import btn_lang


def deliver_or_not(lang: str):
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.insert(KeyboardButton(btn_lang["himself"][lang]))
    btn.insert(KeyboardButton(btn_lang["deliver"][lang]))
    return btn
