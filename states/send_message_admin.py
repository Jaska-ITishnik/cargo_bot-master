from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminSendMessage(StatesGroup):
    message = State()
