from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.translate import btn_lang


def get_main_btn(lang):
    msgs = btn_lang['main_menu']
    res = ReplyKeyboardMarkup(row_width=2)
    res.row(KeyboardButton(text=msgs['trek_code'][lang]), KeyboardButton(text=msgs['admin_panel'][lang]))
    res.row(KeyboardButton(text=msgs['my_id'][lang]), KeyboardButton(text=msgs['get_address'][lang]))
    res.row(KeyboardButton(text=msgs['settings'][lang]), KeyboardButton(text=msgs['buy_yuan'][lang]))
    res.row(KeyboardButton(text=msgs['comments'][lang]), KeyboardButton(text="🛍 Shopping"))
    return res
