from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import OPERATOR
from data.translate import msg_lang
from loader import dp, db, bot
from states.leave_comment import Comment
from keyboards.default.cancel import cancel_btn
from keyboards.default.main_menu import get_main_btn


@dp.message_handler(lambda msg: "💬" in msg.text)
async def leave_comment(msg: types.Message):
    print(db.select_user(tg_id=msg.from_user.id))
    lang = (db.select_user(tg_id=msg.from_user.id))['lang']

    msg_txt = msg_lang["leave_comment"][lang]
    btn = cancel_btn(lang)
    await msg.answer(msg_txt, reply_markup=btn)
    await Comment.first()


@dp.message_handler(state=Comment.desc)
async def leave_comment(msg: types.Message, state: FSMContext):
    lang = db.select_user(tg_id=msg.from_user.id)
    btn = get_main_btn(lang['lang'])
    if msg.text in ("Отмена", "Bekor qilish"):
        txt = msg_lang["main_menu"][lang['lang']]
        await msg.answer(txt, reply_markup=btn)
        await state.finish()
        return
    msg_txt = msg_lang["success_comment"][lang['lang']]
    await msg.answer(msg_txt, reply_markup=btn)
    await state.finish()
    db.create_comment(lang['id'], msg.text)
    msg_txt = f"<b>ID kod:</b> {lang['id_code']}\n<b>Ismi:</b> {lang['full_name']}\n<b>Telefon raqami:</b> {lang['phone_number']}\n\n<b>Comment:</b> {msg.text}"
    await bot.send_message(OPERATOR, msg_txt)
