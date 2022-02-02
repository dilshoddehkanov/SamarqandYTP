import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.config import ADMINS
from loader import dp, dbu, bot, dbcu, dbc, dbs


# @dp.message_handler(text="/allusers", user_id=ADMINS)
# async def get_all_users(message: types.Message):
#     users = dbu.select_all_users()
#     print(users[0][0])
#     await message.answer(users)


@dp.message_handler(text="/cleandbcu", user_id=ADMINS)
async def get_all_users(message: types.Message):
    dbcu.delete_users()
    await message.answer("Baza tozalandi!")


@dp.message_handler(text='/cleandbc', user_id=ADMINS)
async def delete_users(message: types.Message):
    dbc.delete_courses()
    await message.answer("Baza tozalandi!")


@dp.message_handler(text="/delete", user_id=ADMINS)
async def get_all_users(message: types.Message, state: FSMContext):
    courses = dbc.select_all_courses()
    if courses:
        msg = ''
        for course in courses:
            stri = str(course)
            msg = msg + stri + ' \n'
        await message.answer(msg)
        await message.answer('Yuqoridagi kurslar orasidan o\'chirmoqchi bo\'lgan kursingizni id raqamini yuboring.')
        await state.set_state('del_id')
    else:
        await message.answer('🚫Kurslar bazasi bo\'sh!')


@dp.message_handler(state='del_id', user_id=ADMINS)
async def get_all_users(message: types.Message, state: FSMContext):
    del_id = message.text
    del_id = int(del_id)
    dbc.delete_course(del_id)
    await message.answer('Kurs bazadan olib tashlandi')
    await state.finish()


@dp.message_handler(text='/news', user_id=ADMINS)
async def set_news(message: types.Message, state: FSMContext):
    await message.answer('Yangilikni yuboring.')
    await state.set_state('news')


@dp.message_handler(state='news')
async def write_news(message: types.Message, state: FSMContext):
    news = message.text
    users = dbu.select_all_users()
    try:
        for user in users:
            await bot.send_message(text=news, chat_id=user[0])
    except Exception as err:
        print(err)
    await state.finish()


@dp.message_handler(text='/del_user')
async def delete_users(message: types.Message, state: FSMContext):
    all_course = dbc.select_all_courses()
    if all_course:
        courses = []
        a = []
        c = []
        d = []
        e = []
        for i in all_course:
            if len(a) < 3:
                b = KeyboardButton(text=f'{i[2]}')
                a.append(b)
            elif len(a) == 3 and len(c) < 3:
                b = KeyboardButton(text=f'{i[2]}')
                c.append(b)
            elif len(a) == 3 and len(c) == 3 and len(d) < 3:
                b = KeyboardButton(text=f'{i[2]}')
                d.append(b)
            elif len(a) == 3 and len(c) == 3 and len(d) == 3 and len(e) < 3:
                b = KeyboardButton(text=f'{i[2]}')
                e.append(b)
        courses.append(a)
        courses.append(c)
        courses.append(d)
        courses.append(e)
        user_id = message.from_user.id
        user = dbu.select_user(id=user_id)
        if user[2] == 'uz':
            mainmenu = [KeyboardButton(text='Asosiy menu')]
        else:
            mainmenu = [KeyboardButton(text='Главное меню')]
        courses.append(mainmenu)
        coursesKeyboard = ReplyKeyboardMarkup(keyboard=courses,
                                              resize_keyboard=True)
        if user[2] == 'uz':
            await message.answer('Foydalanuvchilarini o\'chirmoqchi bo\'lgan kursingizni tanlang👇👇👇',
                                 reply_markup=coursesKeyboard)
        else:
            await message.answer('Выберите курс, из которого вы хотите удалить пользователей👇👇👇',
                                 reply_markup=coursesKeyboard)
    else:
        await message.answer('🚫Hozircha hech qanday kurs mavjud emas.')
    await state.set_state('del_user')


@dp.message_handler(state='del_user')
async def del_users(message: types.Message, state: FSMContext):
    course = message.text
    course_users = dbcu.select_all_users()
    for course_user in course_users:
        if course_user[1] == course:
            dbcu.delete_course(id=course_user[0])
    await message.answer(f'{course} ga yozilgan foydalanuvchilar bazadan o\'chirildi')
    await state.finish()


@dp.message_handler(text="/del_service", user_id=ADMINS)
async def get_all_users(message: types.Message, state: FSMContext):
    services = dbs.select_all_services()
    if services:
        msg = ''
        for service in services:
            stri = str(service)
            msg = msg + stri + ' \n'
        await message.answer(msg)
        await message.answer('Yuqoridagi xizmatlar orasidan o\'chirmoqchi bo\'lgan xizmatingizni id raqamini yuboring.')
        await state.set_state('delid')
    else:
        await message.answer('🚫Xizmatlar bazasi bo\'sh!')


@dp.message_handler(state='delid', user_id=ADMINS)
async def get_all_users(message: types.Message, state: FSMContext):
    del_id = message.text
    del_id = int(del_id)
    dbs.delete_service(del_id)
    await message.answer('Xizmat bazadan olib tashlandi')
    await state.finish()
