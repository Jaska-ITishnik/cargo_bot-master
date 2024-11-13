from aiogram.dispatcher.filters.state import StatesGroup, State


class Trek_code(StatesGroup):
    code = State()
    deliver_type = State()
    get_location = State()
