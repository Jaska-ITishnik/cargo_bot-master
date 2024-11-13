from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType, ReplyKeyboardRemove

from data.translate import msg_lang, manzils, allows
from keyboards.default.main_menu import get_main_btn
from keyboards.default.register_btn import send_phone, send_location, choose_manzil
from keyboards.inline.register import phone_number2
from loader import dp, db, bot
from states.register import CreateUser, Login, ChooseLang
from utils.own_funcs import get_idcode, download_user_passport, valid_phone, download_user_image, get_passport1, \
    get_passport2

register_lang = msg_lang['register']
login_lang = msg_lang['login']


@dp.callback_query_handler(lambda c: c.data.startswith('auth'), state=ChooseLang.lang)
async def auth_handler(call: types.CallbackQuery, state: FSMContext):
    data = call.data.split('_')[1]
    print(await state.get_data(), state)
    lang = (await state.get_data())['lang']
    await state.finish()
    if data == 'register':
        await call.message.edit_text(register_lang['full_name'][lang])
        await CreateUser.first()
    else:
        await call.message.edit_text(login_lang['phone'][lang])
        await Login.first()
    await state.update_data(lang=lang)


@dp.message_handler(state=CreateUser.full_name)
async def register_fullname(msg: types.Message, state: FSMContext):
    await state.update_data(full_name=msg.text)
    lang = (await state.get_data())['lang']
    await msg.answer(register_lang['phone'][lang], reply_markup=send_phone(lang))
    await CreateUser.next()


@dp.message_handler(state=CreateUser.phone_number, content_types=ContentType.CONTACT)
async def register_phone(msg: types.Message, state: FSMContext):
    lang = (await state.get_data())['lang']
    users = db.selects_users(phone_number=msg.text)
    if users:
        await msg.answer(msg_lang['error_phone'][lang])
        return
    await state.update_data(phone_number=msg.contact.phone_number)
    await msg.answer(register_lang['if_phone2'][lang], reply_markup=phone_number2(lang))


@dp.callback_query_handler(lambda call: call.data.startswith('phone2'), state=CreateUser.phone_number)
async def register_phone_callback(call: types.CallbackQuery, state: FSMContext):
    sep = call.data.split('_')[1]
    lang = (await state.get_data())['lang']
    if sep == 'yes':
        await call.message.edit_text(register_lang['phone2'][lang])
        await CreateUser.next()
    else:
        await call.message.delete()
        await call.message.answer_photo(get_passport1(), register_lang['passport1'][lang])
        await CreateUser.passport1.set()


@dp.message_handler(state=CreateUser.phone_number)
async def register_phone(msg: types.Message, state: FSMContext):
    lang = (await state.get_data())['lang']
    await msg.answer(msg_lang['not_phone'][lang])


@dp.message_handler(state=CreateUser.phone_number2)
async def register_phone(msg: types.Message, state: FSMContext):
    lang = (await state.get_data())['lang']
    valid = valid_phone(msg.text, lang)
    if valid != msg.text:
        await msg.answer(valid)
        return
    users = db.selects_users(phone_number2=msg.text)
    if users:
        await msg.answer(msg_lang['error_phone'][lang])
        return
    await state.update_data(phone_number2=msg.text)
    await msg.answer_photo(get_passport1(), register_lang['passport1'][lang])
    await CreateUser.next()


@dp.message_handler(content_types=ContentType.PHOTO, state=CreateUser.passport1)
async def register_passport1(msg: types.Message, state: FSMContext):
    lang = (await state.get_data())['lang']
    passport1 = await download_user_passport(msg.photo[-1]['file_id'])
    await state.update_data(passport1=passport1)
    await msg.answer_photo(get_passport2(), register_lang['passport2'][lang])
    await CreateUser.next()


@dp.message_handler(content_types=ContentType.PHOTO, state=CreateUser.passport2)
async def register_passport2(msg: types.Message, state: FSMContext):
    passport2 = await download_user_passport(msg.photo[-1]['file_id'])
    lang = (await state.get_data())['lang']
    await state.update_data(passport2=passport2)
    await msg.answer(register_lang['image'][lang])
    await CreateUser.next()


@dp.message_handler(content_types=ContentType.PHOTO, state=CreateUser.image)
async def register_passport2(msg: types.Message, state: FSMContext):
    image = await download_user_image(msg.photo[-1]['file_id'])
    lang = (await state.get_data())['lang']
    await state.update_data(image=image)
    await msg.answer(register_lang['address'][lang], reply_markup=send_location(lang))
    await CreateUser.next()


@dp.message_handler(state=CreateUser.image)
async def register_passport1(msg: types.Message, state: FSMContext):
    lang = (await state.get_data())['lang']
    await msg.answer(msg_lang['error_image'][lang])


@dp.message_handler(state=CreateUser.passport1)
@dp.message_handler(state=CreateUser.passport2)
async def register_passport1(msg: types.Message, state: FSMContext):
    lang = (await state.get_data())['lang']
    await msg.answer(msg_lang['error_passport'][lang])


@dp.message_handler(state=CreateUser.address, content_types=ContentType.LOCATION)
async def register_address(msg: types.Message, state: FSMContext):
    await state.update_data(latitude=msg.location.latitude, longitude=msg.location.longitude)
    lang = (await state.get_data())['lang']
    await msg.answer(register_lang['manzil'][lang], reply_markup=ReplyKeyboardRemove())
    manz = {
        0: 'A',
        1: 'B',
        2: 'C'
    }
    id_code = get_idcode()
    for manzil in manzils:
        code = manz[manzil] + id_code
        m = manzils[manzil][lang].format(code=code[1:]) + '\n\n\n' + '<b>' + msg_lang['allow'][
            lang].upper() + '</b>' + '\n\n' + allows[manzil][
                lang]
        await msg.answer(m)

    data = await state.get_data()
    await state.finish()
    lang = data['lang']
    full_name = data['full_name']
    phone_number = data['phone_number']
    phone_number2 = data.get('phone_number2', None)
    passport1 = data['passport1']
    passport2 = data['passport2']
    image = data['image']
    latitude = data['latitude']
    longitude = data['longitude']
    tg_id = msg.from_user.id
    user = db.select_user(tg_id=tg_id)
    if user:
        db.update_user_by_id(
            tg_id,
            lang=lang,
            full_name=full_name,
            phone_number=phone_number,
            phone_number2=phone_number2,
            passport1=passport1,
            passport2=passport2,
            image=image,
            latitude=latitude,
            longitude=longitude,
            id_code=id_code,
            is_active=True,
            is_standart=False,
            is_kg=False,
            types="A"
        )
    else:
        db.create_user(
            lang=lang,
            full_name=full_name,
            phone_number=phone_number,
            phone_number2=phone_number2,
            passport1=passport1,
            passport2=passport2,
            image=image,
            latitude=latitude,
            longitude=longitude,
            id_code=id_code,
            tg_id=tg_id,
            is_active=True,
            is_standart=False,
            is_kg=False,
            referal_id=None,
            types="A"
        )
    await msg.answer(msg_lang['greeting'][lang].format(msg.from_user.first_name),
                     reply_markup=get_main_btn(lang))


@dp.message_handler(state=CreateUser.address)
async def register_address(msg: types.Message, state: FSMContext):
    lang = (await state.get_data())['lang']
    await msg.answer(msg_lang['not_address'][lang])
