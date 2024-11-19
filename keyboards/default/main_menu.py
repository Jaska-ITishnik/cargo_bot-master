from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.config import ADMINS
from data.translate import btn_lang


def get_main_btn(lang, msg):
    msgs = btn_lang['main_menu']
    res = ReplyKeyboardMarkup(row_width=2)
    if str(msg.from_user.id) in ADMINS:
        res.row(KeyboardButton(text=msgs['admin_panel'][lang]), KeyboardButton(text=msgs['admin_send_message'][lang]))
    res.row(KeyboardButton(text=msgs['trek_code'][lang]))
    res.row(KeyboardButton(text=msgs['my_id'][lang]), KeyboardButton(text=msgs['get_address'][lang]))
    res.row(KeyboardButton(text=msgs['settings'][lang]), KeyboardButton(text=msgs['buy_yuan'][lang]))
    res.row(KeyboardButton(text=msgs['comments'][lang]), KeyboardButton(text="🛍 Shopping"))
    return res
