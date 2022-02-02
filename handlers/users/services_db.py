from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.default.LanguageKeyboard import Main_Menu_uz
from loader import dp, dbc, dbs


@dp.message_handler(text='/service', user_id=ADMINS)
async def create_course(message: Message, state: FSMContext):
    await message.answer('Xizmat nomini kiriting: ', reply_markup=ReplyKeyboardRemove())
    await state.set_state('name_service')


@dp.message_handler(state='name_service', user_id=ADMINS)
async def write_name(message: Message, state: FSMContext):
    name = message.text
    services = dbs.select_all_services()
    if not services:
        count = 0
    else:
        service = services[-1]
        count = service[0]
    dbs.add_service(id=count + 1, name=message.from_user.full_name, service=name)
    await message.answer(f'Xizmat haqida ma\'lumot yozing(o\'zbek tilida)')
    await state.set_state('informationuz')


@dp.message_handler(state='informationuz', user_id=ADMINS)
async def write_information(message: Message, state: FSMContext):
    information = message.text
    services = dbs.select_all_services()
    service = services[-1]
    dbs.update_informationuz(id=service[0], informationuz=information)
    await message.answer('Xizmat haqida ma\'lumot yozing(rus tilida)')
    await state.set_state('informationru')


@dp.message_handler(state='informationru', user_id=ADMINS)
async def write_informationru(message: Message, state: FSMContext):
    information = message.text
    services = dbs.select_all_services()
    service = services[-1]
    dbs.update_informationru(id=service[0], informationru=information)
    await message.answer('Xizmat uchun rasm tashlang: ')
    await state.set_state('photo_service')


@dp.message_handler(content_types=types.ContentType.PHOTO, state='photo_service')
async def photo_course(message: Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    services = dbs.select_all_services()
    service = services[-1]
    dbs.update_photo(id=service[0], photo=photo_id)
    await message.answer(f'✅{service[2]} bazaga qo\'shildi.', reply_markup=Main_Menu_uz)
    await state.finish()
