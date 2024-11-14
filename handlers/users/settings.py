from aiogram import types
from aiogram.dispatcher import FSMContext

from data.translate import msg_lang
from keyboards.default.main_menu import get_main_btn
from keyboards.inline.choose_lang import settings_btn, change_lang_btn
from keyboards.default.cancel import cancel_btn
from loader import dp, db
from states.settings_state import ChangePhone
from utils.own_funcs import valid_phone


@dp.message_handler(lambda msg: "⚙️" in msg.text)
async def edit_settings(message: types.Message):
    lang = (db.select_user(tg_id=message.from_user.id))['lang']
    msg = msg_lang["settings"][lang]
    await message.answer(msg, reply_markup=settings_btn(lang))


@dp.callback_query_handler(lambda query: query.data.startswith("change"))
async def change_settings(callback: types.CallbackQuery):
    lang = (db.select_user(tg_id=callback.from_user.id))['lang']
    sep = callback.data.split("_")[1]
    if sep == "cancel":
        txt = msg_lang["main_menu"][lang]
        btn = get_main_btn(lang)
        await callback.message.delete()
        await callback.message.answer(txt, reply_markup=btn)
    elif sep == "lang":
        msg = msg_lang["choose_lang"][lang]
        btn = change_lang_btn(lang)
        await callback.message.edit_text(msg, reply_markup=btn)
    else:
        msg = msg_lang["change_phone"][lang]
        btn = cancel_btn(lang)
        await ChangePhone.first()
        await callback.message.delete()
        await callback.message.answer(msg, reply_markup=btn)


@dp.callback_query_handler(lambda query: query.data.startswith("chlang"))
async def change_lang(callback: types.CallbackQuery):
    sep = callback.data.split("_")[1]
    lang = db.select_user(tg_id=callback.from_user.id)
    if sep == "cancel":
        txt = msg_lang["main_menu"][lang['lang']]
        btn = get_main_btn(lang['lang'])
        await callback.message.delete()
        await callback.message.answer(txt, reply_markup=btn)
    else:
        db.update_user_by_id(tg_id=callback.from_user.id, lang=sep)
        msg = msg_lang["success_lang"][sep]
        btn = get_main_btn(sep)
        await callback.message.delete()
        await callback.message.answer(msg, reply_markup=btn)


@dp.message_handler(state=ChangePhone.phone)
async def change_phone(message: types.Message, state: FSMContext):
    await state.finish()
    phone = message.text
    lang = (db.select_user(tg_id=message.from_user.id))['lang']
    if phone in ("Отмена", "Bekor qilish"):
        txt = msg_lang["main_menu"][lang]
        btn = get_main_btn(lang)
        await message.answer(txt, reply_markup=btn)
        await state.finish()
        return
    valid = valid_phone(phone, lang)
    if valid != phone:
        await message.answer(valid)
        return
    db.update_user_by_id(tg_id=message.from_user.id, phone_number=phone[1:])
    msg = msg_lang["success_phone"][lang]
    btn = get_main_btn(lang)
    await message.answer(msg, reply_markup=btn)
