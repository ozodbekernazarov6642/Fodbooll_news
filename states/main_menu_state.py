from aiogram.dispatcher.filters.state import State, StatesGroup


class Main_State(StatesGroup):
    user_main = State()
    search = State()
    Tournaments = State()
    match_center = State()


class Tournament_state(StatesGroup):
    liga = State()
    departments = State()


class Complaints(StatesGroup):
    send_group = State()
    confirmation= State()
