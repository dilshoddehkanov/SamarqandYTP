from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.default.LanguageKeyboard import Main_Menu_uz
from loader import dp, dbc


@dp.message_handler(text='/courses', user_id=ADMINS)
async def create_course(message: Message, state: FSMContext):
    await message.answer('Kurs nomini kiriting: ', reply_markup=ReplyKeyboardRemove())
    await state.set_state('name_course')


@dp.message_handler(state='name_course', user_id=ADMINS)
async def write_name(message: Message, state: FSMContext):
    name = message.text
    courses = dbc.select_all_courses()
    if not courses:
        count = 0
    else:
        course = courses[-1]
        count = course[0]
    dbc.add_user(id=count + 1, name=message.from_user.full_name, course=name)
    await message.answer(f'Kurs haqida ma\'lumot yozing(o\'zbek tilida)')
    await state.set_state('information_uz')


@dp.message_handler(state='information_uz', user_id=ADMINS)
async def write_information(message: Message, state: FSMContext):
    information = message.text
    courses = dbc.select_all_courses()
    course = courses[-1]
    dbc.update_informationuz(id=course[0], informationuz=information)
    await message.answer('Kurs haqida ma\'lumot yozing(rus tilida)')
    await state.set_state('information_ru')


@dp.message_handler(state='information_ru', user_id=ADMINS)
async def write_informationru(message: Message, state: FSMContext):
    information = message.text
    courses = dbc.select_all_courses()
    course = courses[-1]
    dbc.update_informationru(id=course[0], informationru=information)
    await message.answer('Kurs uchun rasm tashlang: ')
    await state.set_state('photo_course')


@dp.message_handler(content_types=types.ContentType.PHOTO, state='photo_course', user_id=ADMINS)
async def photo_course(message: Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    courses = dbc.select_all_courses()
    course = courses[-1]
    dbc.update_photo(id=course[0], photo_id=photo_id)
    await message.answer(f'✅{course[2]} bazaga qo\'shildi.', reply_markup=Main_Menu_uz)
    await state.finish()


