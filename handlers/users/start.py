import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from keyboards.default.LanguageKeyboard import language, Main_Menu_uz, Main_Menu_ru
from loader import dp, bot, dbu


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        dbu.add_user(id=message.from_user.id,
                     name=name)
    except sqlite3.IntegrityError as err:
        pass

    await message.answer(f"Assalomu aleykum {message.from_user.full_name}.\n"
                         f"Samarqand Viloyati Yoshlar Inavatsion Texnoparkining rasmiy botiga xush kelibsiz!")
    await message.answer("Tilni tanlang👇👇👇", reply_markup=language)
    await state.finish()
    # Adminga xabar beramiz
    # count = dbu.count_users()[0]
    # msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    # await bot.send_message(chat_id=ADMINS[0], text=msg)


@dp.message_handler(text='🇺🇿UZ')
@dp.message_handler(text='Asosiy menu', state='*')
async def choose_language(message: types.Message, state: FSMContext):
    dbu.update_language(id=message.from_user.id, language='uz')
    await message.answer('Asosiy menu', reply_markup=Main_Menu_uz)
    await state.finish()


@dp.message_handler(text='🇷🇺RU')
@dp.message_handler(text='Главное меню', state='*')
async def choose_language(message: types.Message, state: FSMContext):
    dbu.update_language(id=message.from_user.id, language='ru')
    await message.answer('Главное меню', reply_markup=Main_Menu_ru)
    await state.finish()
