from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

language = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🇺🇿UZ'),
            KeyboardButton(text='🇷🇺RU'),
        ],
    ],
    resize_keyboard=True
)


Main_Menu_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📚Kurslar haqida'),
            KeyboardButton(text='🖌Kursga yozilish')
        ],
        [
            KeyboardButton(text='🛠Xizmatlar'),
            KeyboardButton(text='🏢Samarqamd Yoshlar TexnoParki haqida'),
        ],
    ],
    resize_keyboard=True
)


Main_Menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📚О курсах'),
            KeyboardButton(text='🖌Запись на курс'),
        ],
        [
            KeyboardButton(text='🛠Сервисы'),
            KeyboardButton(text='🏢О Самаркандском Молодежном Технопарке')
        ],
    ],
    resize_keyboard=True
)
