from aiogram.dispatcher.filters.state import StatesGroup, State


class Comment(StatesGroup):
    desc = State()
