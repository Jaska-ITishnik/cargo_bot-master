from aiogram.dispatcher.filters.state import StatesGroup, State


class ChooseLang(StatesGroup):
    lang = State()


class CreateUser(StatesGroup):
    full_name = State()
    phone_number = State()
    phone_number2 = State()
    passport1 = State()
    passport2 = State()
    image = State()
    address = State()


class Login(StatesGroup):
    phone_number = State()
    id_code = State()
