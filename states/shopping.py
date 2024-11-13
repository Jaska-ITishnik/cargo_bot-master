from aiogram.dispatcher.filters.state import StatesGroup, State


class Shopping(StatesGroup):
    link = State()
    image = State()
