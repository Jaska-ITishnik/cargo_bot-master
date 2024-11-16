from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import YUAN_BOT
from data.translate import btn_lang

langs = InlineKeyboardMarkup(row_width=2)
langs.insert(InlineKeyboardButton("🇺🇿 O'zbek tili", callback_data="lang_uz"))
langs.insert(InlineKeyboardButton("🇷🇺 Русский язык", callback_data="lang_ru"))


def settings_btn(lang):
    txt = btn_lang["settings"]
    res = InlineKeyboardMarkup(row_width=2)
    res.insert(InlineKeyboardButton(txt["lang"][lang], callback_data="change_lang"))
    res.insert(InlineKeyboardButton(txt["phone"][lang], callback_data="change_phone"))
    res.insert(
        InlineKeyboardButton(btn_lang["cancel"][lang], callback_data="change_cancel")
    )
    return res


def change_lang_btn(lang):
    res = InlineKeyboardMarkup(row_width=2)
    res.insert(InlineKeyboardButton("🇺🇿 O'zbek tili", callback_data="chlang_uz"))
    res.insert(InlineKeyboardButton("🇷🇺 Русский язык", callback_data="chlang_ru"))
    res.insert(
        InlineKeyboardButton(btn_lang["cancel"][lang], callback_data="chlang_cancel")
    )

    return res


def buy_yuan(lang):
    res = InlineKeyboardMarkup(row_width=1)
    res.insert(InlineKeyboardButton("""
                    Texnik sabablarga ko'ra 
                    YUAN bot ishlamayapti 👷
                    """))
    return res
