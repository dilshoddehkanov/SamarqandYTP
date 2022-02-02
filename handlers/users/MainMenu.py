from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp, dbc, dbu, bot, dbs


@dp.message_handler(text='📚Kurslar haqida')
@dp.message_handler(text='📚О курсах')
async def courses_yoz(message: Message):
    all_course = dbc.select_all_courses()
    if all_course:
        courses = []
        a = []
        c = []
        d = []
        e = []
        for i in all_course:
            if len(a) < 3:
                b = KeyboardButton(text=f'📘 {i[2]}')
                a.append(b)
            elif len(a) == 3 and len(c) < 3:
                b = KeyboardButton(text=f'📘 {i[2]}')
                c.append(b)
            elif len(a) == 3 and len(c) == 3 and len(d) < 3:
                b = KeyboardButton(text=f'📘 {i[2]}')
                d.append(b)
            elif len(a) == 3 and len(c) == 3 and len(d) == 3 and len(e) < 3:
                b = KeyboardButton(text=f'📘 {i[2]}')
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
            await message.answer('Qaysi kurs haqida ma\'lumot olmoqchi bo\'lsangiz tanlang👇👇👇',
                                 reply_markup=coursesKeyboard)
        else:
            await message.answer('Выберите курс, о котором вы хотите узнать👇👇👇',
                                 reply_markup=coursesKeyboard)
    else:
        await message.answer('🚫Hozircha hech qanday kurs mavjud emas.')


@dp.message_handler(text='🏢Samarqamd Yoshlar TexnoParki haqida')
@dp.message_handler(text='🏢О Самаркандском Молодежном Технопарке')
async def info(message: Message):
    user_id = message.from_user.id
    user = dbu.select_user(id=user_id)
    if user[2] == 'uz':
        await bot.send_message(
            text="<b>\"Samarqand Viloyati yoshlar texnoparki\" mas\'uliyati cheklangan jamiyati</b>\n\n"
                 "<b>Faoliyati:</b> Samarqand Viloyati yoshlar texnoparki yoshlarni ilmiy tadqiqot va"
                 "innovatsion faoliyatga keng jalb etish, iqtidorli yoshlarning intelektual salohiyatini, "
                 "ilmiy-texnik, innovatsion va startap-loyihalarni amaliyotga yo\'naltiradi.\n\n"
                 "<b>Ro\'yxatdan o\'tgan sana: </b>09.09.2021\n"
                 "<b>Ro\'yxatdan o\'tkazuvchi organ:</b> Davlat xizmatlari markazi\n"
                 "<b>STIR:</b> 308844099\n"
                 "<b>THSHT</b> 152-Mas\'uliyati cheklangan yoki qo\'shimcha mas\'uliyatli jamiyat\n"
                 "<b>DBIBT</b> 79994-Davlat va xo\'jalik boshqaruvi organlari tarkibiga kirmagan "
                 "tadbirkorlik sub\'yektlari\n"
                 "<b>IFUT</b> 72190-Tabiiy fanlar va injeneriya sohasidagi boshqa tadqiqotlar va "
                 "ishlanmalar\n\n", chat_id=message.from_user.id)
        await message.answer("*Kontakt\(a\'loqa\) ma\'lumotlari:*\n\n"
                             "📱Telefon raqam:  \+998889345505\n"
                             "📎Bog\'lanish uchun: \@samytp\_uz\n"
                             "📍Manzil: Samarqand shahri, Universitet xiyoboni ko\'chasi, 15\-uy\n"
                             "📍Mo\'ljal: SamDU tarix fakulteti kirish binosi, 6\-talabalar turar joyi binosi yonida\n"
                             "Elektron pochta: samytp@gmail\.com\n\n"
                             "*Rahbar: Muxsinov Komil Vakilovich*\n\n"
                             "Ijtimoiy tarmoqlar👇👇👇\n" +
                             "[Instagram](https://www.instagram.com/samytpuz) \| "
                             "[Facebook](https://www.facebook.com/samytpuz) \| "
                             "[Telegram](https://t.me/samytp)", parse_mode=types.ParseMode.MARKDOWN_V2)
    else:
        await bot.send_message(
            text="<b> \"Общество с Ограниченной Ответственностью Самаркандского Областного Молодёжного Технопарка</b> \n\n"
                 "<b> Деятельность: </b> Самаркандский областной молодежный технопарк для научных исследований и"
                 "широкое вовлечение в инновационную деятельность, интеллектуальный потенциал талантливой молодежи,"
                 "Реализует научно-технические, инновационные и стартап-проекты.\n\n"
                 "<b> Дата регистрации: </b> 09.09.2021\n"
                 "<b>Регистрационный орган: </b>Центр государственных услуг\n"
                 "<b> ПЕРЕМЕЩЕНИЕ: </b> 308844099 \ n"
                 "<b> ТХШТ </b> 152-Общество с ограниченной ответственностью или общество с дополнительной ответственностью\n"
                 "<b> ДБИБТ </b> 79994-Не входит в состав государственного и хозяйственного управления"
                 "субъекты хозяйствования"
                 "<b>ИФУТ</b> 72190-Прочие исследования в области естественных и технических наук и"
                 "развития\n\n", chat_id=message.from_user.id)
        await message.answer("*Контактная информация: *\n\n"
                             "📱Номер телефона: \+998935144148\n"
                             "📎Контакты: \@samytp \_uz \n"
                             "📍Адрес: город Самарканд, Университетский проспект, дом 15\n"
                             "📍Назначение: Входной корпус исторического факультета СамГУ, рядом с корпусом 6\-студенческого общежития\n"
                             "Электронная почта: samytp@gmail\.com\n\n"
                             "*Руководитель: Мухсинов Комил Вакилович*\n\n"
                             "Социальные сети👇👇👇\n" +
                             "[Instagram](https://www.instagram.com/samytpuz) \| "
                             "[Facebook](https://www.facebook.com/samytpuz) \| "
                             "[Telegram](https://t.me/samytp)", parse_mode=types.ParseMode.MARKDOWN_V2)


@dp.message_handler(Text(contains='📘', ignore_case=True))
async def course_inform(message: Message):
    course_name = message.text.replace('📘 ', '')
    course = dbc.select_course(course=course_name)
    user_id = message.from_user.id
    user = dbu.select_user(id=user_id)
    if user[2] == 'uz':
        course_inline = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='✒️Kursga yozilish', callback_data=f'course{course[2]}')
                ]
            ]
        )
        await message.reply_photo(photo=course[5], caption=course[3], reply_markup=course_inline)
    else:
        course_inline = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='✒️Записаться на курс', callback_data=f'course{course[2]}')
                ]
            ]
        )
        await message.reply_photo(photo=course[5], caption=course[4], reply_markup=course_inline)


@dp.message_handler(text='🛠Xizmatlar')
@dp.message_handler(text='🛠Сервисы')
async def courses_yoz(message: Message):
    all_service = dbs.select_all_services()
    user_id = message.from_user.id
    user = dbu.select_user(id=user_id)
    if all_service:
        services = []
        a = []
        c = []
        d = []
        e = []
        for i in all_service:
            if len(a) < 3:
                b = KeyboardButton(text=f'⚒ {i[2]}')
                a.append(b)
            elif len(a) == 3 and len(c) < 3:
                b = KeyboardButton(text=f'⚒ {i[2]}')
                c.append(b)
            elif len(a) == 3 and len(c) == 3 and len(d) < 3:
                b = KeyboardButton(text=f'⚒ {i[2]}')
                d.append(b)
            elif len(a) == 3 and len(c) == 3 and len(d) == 3 and len(e) < 3:
                b = KeyboardButton(text=f'⚒ {i[2]}')
                e.append(b)
        services.append(a)
        services.append(c)
        services.append(d)
        services.append(e)
        if user[2] == 'uz':
            mainmenu = [KeyboardButton(text='Asosiy menu')]
        else:
            mainmenu = [KeyboardButton(text='Главное меню')]
        services.append(mainmenu)
        servicesKeyboard = ReplyKeyboardMarkup(keyboard=services,
                                              resize_keyboard=True)
        if user[2] == 'uz':
            await message.answer('Qaysi xizmat haqida ma\'lumot olmoqchi bo\'lsangiz tanlang👇👇👇',
                                 reply_markup=servicesKeyboard)
        else:
            await message.answer('Выберите, о какой услуге вы хотите узнать👇👇👇',
                                 reply_markup=servicesKeyboard)
    else:
        if user[2] == 'uz':
            await message.answer('🚫Hozircha hech qanday xizmat mavjud emas.')
        else:
            await message.answer('🚫Услуга пока недоступна.')


@dp.message_handler(Text(contains='⚒', ignore_case=True))
async def course_inform(message: Message):
    service_name = message.text.replace('⚒ ', '')
    service = dbs.select_service(service=service_name)
    user_id = message.from_user.id
    user = dbu.select_user(id=user_id)
    if user[2] == 'uz':
        await message.reply_photo(photo=service[5], caption=service[3])
    else:
        await message.reply_photo(photo=service[5], caption=service[4])
