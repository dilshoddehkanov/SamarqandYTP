from aiogram.dispatcher import FSMContext
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, CallbackQuery

from data.config import ADMINS
from keyboards.default.LanguageKeyboard import Main_Menu_uz, Main_Menu_ru
from loader import dp, dbu, dbc, dbcu, bot
from states.course_write import CourseUser


@dp.message_handler(text='🖌Kursga yozilish')
@dp.message_handler(text='🖌Запись на курс')
async def take_phone(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = dbu.select_user(id=user_id)
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
            await message.answer('Yozilmoqchi bo\'lgan kursingizni tanlang👇👇👇',
                                 reply_markup=coursesKeyboard)
        else:
            await message.answer('Выберите курс, на который хотите записаться👇👇👇',
                                 reply_markup=coursesKeyboard)
        await CourseUser.course_write.set()
    else:
        await message.answer('🚫Hozircha hech qanday kurs mavjud emas.')


@dp.message_handler(state=CourseUser.course_write)
async def course_name(message: Message, state: FSMContext):
    courses_name = message.text
    courses = dbcu.select_all_users()
    count = len(courses)
    dbcu.add_courseuser(id=count + 1, course=courses_name)
    user_id = message.from_user.id
    user = dbu.select_user(id=user_id)
    if user[2] == 'uz':
        await message.answer('Telefon raqamingizni yuboring', reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer('Отправьте свой номер телефона', reply_markup=ReplyKeyboardRemove())
    await CourseUser.next()


@dp.message_handler(state=CourseUser.phone_num)
async def take_full_name(message: Message, state: FSMContext):
    phone_num = message.text
    courses = dbcu.select_all_users()
    count = len(courses)
    dbcu.update_phone_num(id=count, phone_num=phone_num)
    user_id = message.from_user.id
    user = dbu.select_user(id=user_id)
    if user[2] == 'uz':
        await message.answer('To\'liq ism-familiyangizni kiriting.')
    else:
        await message.answer('Введите свое полное имя.')
    await CourseUser.next()


@dp.message_handler(state=CourseUser.full_name)
async def take_address(message: Message, state: FSMContext):
    full_name = message.text
    courses = dbcu.select_all_users()
    count = len(courses)
    dbcu.update_full_name(id=count, full_name=full_name)
    user_id = message.from_user.id
    user = dbu.select_user(id=user_id)
    if user[2] == 'uz':
        await message.answer('Manzilingizni yozib yuboring.')
    else:
        await message.answer('Введите свой адрес.')
    await CourseUser.next()


@dp.message_handler(state=CourseUser.address)
async def take_address(message: Message, state: FSMContext):
    address = message.text
    user_id = message.from_user.id
    user = dbu.select_user(id=user_id)
    courses = dbcu.select_all_users()
    count = len(courses)
    dbcu.update_adress(id=count, address=address)
    if user[2] == 'uz':
        await message.answer('Tug\'ilgan yilingizni kiriting.')
    else:
        await message.answer('Введите свой год рождения.')
    await CourseUser.next()


@dp.message_handler(state=CourseUser.birth_year)
async def take_birth_year(message: Message, state: FSMContext):
    birth_year = message.text
    user_id = message.from_user.id
    user = dbu.select_user(id=user_id)
    courses = dbcu.select_all_users()
    count = len(courses)
    dbcu.update_birth_year(id=count, birth_year=birth_year)
    if user[2] == 'uz':
        await message.answer('Sizga qaysi kunla qulay? (Juft/Toq kunlar)')
    else:
        await message.answer('Какой день вам удобен? (четные/нечетные дни)')
    await CourseUser.next()


@dp.message_handler(state=CourseUser.days)
async def take_days(message: Message, state: FSMContext):
    days = message.text
    user_id = message.from_user.id
    user = dbu.select_user(id=user_id)
    courses = dbcu.select_all_users()
    count = len(courses)
    dbcu.update_days(id=count, days=days)
    if user[2] == 'uz':
        await message.answer('Kunning qaysi qismi qulay siz uchun? (Masalan, 09:00-11:00)')
    else:
        await message.answer('Какая часть дня для вас комфортна? (Например, 09:00-11:00)')
    await CourseUser.next()


@dp.message_handler(state=CourseUser.day_time)
async def take_day_time(message: Message, state: FSMContext):
    day_time = message.text
    user_id = message.from_user.id
    user = dbu.select_user(id=user_id)
    courses = dbcu.select_all_users()
    count = len(courses)
    dbcu.update_day_time(id=count, day_time=day_time)
    course = dbcu.select_user(id=count)
    if user[2] == 'uz':
        await message.answer(f'Siz {course[1]} kursiga yozildingiz.', reply_markup=Main_Menu_uz)
    else:
        await message.answer(f'Вы записались на курс {course[1]}.', reply_markup=Main_Menu_ru)
    await bot.send_message(ADMINS[0], f'✅ {message.from_user.full_name} {course[1]} kursiga yozildi.')
    await state.finish()


@dp.callback_query_handler(text_startswith='course')
async def course_write(query: CallbackQuery, state: FSMContext):
    coursename = query.data.replace('course', '')
    courses = dbcu.select_all_users()
    count = len(courses)
    dbcu.add_courseuser(id=count + 1, course=coursename)
    user_id = query.message.reply_to_message.from_user.id
    user = dbu.select_user(id=user_id)
    if user[2] == 'uz':
        await query.message.answer('Telefon raqamingizni yuboring', reply_markup=ReplyKeyboardRemove())
    else:
        await query.message.answer('Отправьте свой номер телефона', reply_markup=ReplyKeyboardRemove())
    await CourseUser.phone_num.set()
