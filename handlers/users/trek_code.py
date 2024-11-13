from aiogram import types
from aiogram.dispatcher import FSMContext
from environs import Env
from data.config import OPERATOR
from keyboards.default.cancel import cancel_btn
from states.trek_code import Trek_code
from data.translate import msg_lang
from keyboards.default.main_menu import get_main_btn
from keyboards.default.deliver import deliver_or_not
from keyboards.default.register_btn import send_location
from loader import dp, db, bot

env = Env()
env.read_env()


@dp.message_handler(
    lambda x: x.text in ("🔎 Проверка трек-кода", "🔎 Trek kodini tekshirish")
)
async def trek_code(msg: types.Message):
    lang = db.select_user(tg_id=msg.from_user.id)
    trek_code = db.select_product_trek_code(user_id=lang[0])
    print(trek_code)
    txt = msg_lang["trek_code"][lang[3]]
    btn = cancel_btn(lang[3])
    await msg.answer(txt, reply_markup=btn)
    await Trek_code.first()


@dp.message_handler(state=Trek_code.code)
async def code_ans(msg: types.Message, state=FSMContext):
    lang = db.select_user(tg_id=msg.from_user.id)
    if msg.text in ("Отмена", "Bekor qilish"):
        txt = msg_lang["main_menu"][lang[3]]
        btn = get_main_btn(lang[3])
        await msg.answer(txt, reply_markup=btn)
        await state.finish()
        return
    all_trek_codes_from_db = db.select_product_trek_code(user_id=lang[0])
    trek_codes_list = [i[0] for i in all_trek_codes_from_db]
    if msg.text in trek_codes_list:
        is_arrived_or_is_taken = db.select_product_arrive_taken(trek_code=msg.text)
        if (is_arrived_or_is_taken[0][0] and is_arrived_or_is_taken[0][1]) and True:
            txt = msg_lang["taken"][lang[3]]
            btn = get_main_btn(lang[3])
            await msg.answer(txt, reply_markup=btn)
            await state.finish()
        elif is_arrived_or_is_taken[0][0]:
            txt = msg_lang["deliver_or_not"][lang[3]]
            btn = deliver_or_not(lang[3])
            await msg.answer(txt, reply_markup=btn)
            await Trek_code.next()
        else:
            txt = msg_lang["not_arrived"][lang[3]]
            btn = get_main_btn(lang[3])
            await msg.answer(txt, reply_markup=btn)
            await state.finish()
    else:
        txt = msg_lang["no_trek_code"][lang[3]]
        btn = cancel_btn(lang[3])
        await msg.answer(txt, reply_markup=btn)
        return


@dp.message_handler(state=Trek_code.deliver_type)
async def deliver_type_ans(msg: types.Message, state=FSMContext):
    lang = db.select_user(tg_id=msg.from_user.id)
    if msg.text in ("Забрать самому", "Borib olish"):
        txt = msg_lang["bring_deliver"][lang[3]]
        btn = get_main_btn(lang[3])
        await bot.send_location(
            chat_id=msg.chat.id,
            latitude=env.str("LATITUDE"),
            longitude=env.str("LONGITUDE"),
        )
        await msg.answer(txt, reply_markup=btn)
        await state.finish()
    elif msg.text in (
        "Сделать доставку",
        "Buyurtmani yuborish(dostavka)",
    ):
        txt = msg_lang["deliver"][lang[3]]
        btn = send_location(lang[3])
        await msg.answer(txt, reply_markup=btn)
        await Trek_code.next()
    else:
        return


@dp.message_handler(
    content_types=(types.ContentType.LOCATION, types.ContentType.TEXT),
    state=Trek_code.get_location,
)
async def get_loc_ans(msg: types.Message, state=FSMContext):
    lang = db.select_user(tg_id=msg.from_user.id)
    if msg.text:
        txt = msg_lang["not_address"][lang[3]]
        btn = send_location(lang[3])
        await msg.answer(txt, reply_markup=btn)
        return
    else:
        latitude = msg.location.latitude
        longitude = msg.location.longitude
        print(latitude, longitude)
        db.update_user_loc(latitude, longitude, msg.from_user.id)
        txt = msg_lang["success_deliver"][lang[3]]
        btn = get_main_btn(lang[3])
        await msg.answer(txt, reply_markup=btn)
        await state.finish()
        await bot.send_location(OPERATOR, latitude=latitude, longitude=longitude)
        await bot.send_message(
            chat_id=OPERATOR,
            text=f"New location to delivery❗️\nUsername:{msg.from_user.username}\nPhone:{lang[2]}, {lang[11]}",
        )
