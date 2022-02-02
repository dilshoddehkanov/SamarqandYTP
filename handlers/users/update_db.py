from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from loader import dp, dbu


@dp.message_handler(Command("email"))
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Email manzilingizni yuboring")
    await state.set_state("email")


@dp.message_handler(state="email")
async def enter_email(message: types.Message, state: FSMContext):
    email = message.text
    dbu.update_user_email(email=email, id=message.from_user.id)
    user = dbu.select_user(id=message.from_user.id)
    await message.answer(f"Baza yangilandi: {user}")
    await state.finish()
