from aiogram.dispatcher.filters.state import StatesGroup, State


class CourseUser(StatesGroup):
    course_write =State()
    phone_num =State()
    full_name =State()
    address =State()
    birth_year =State()
    days =State()
    day_time =State()