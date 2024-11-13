from aiogram.dispatcher.filters.state import StatesGroup, State


class ChangePhone(StatesGroup):
    phone = State()
