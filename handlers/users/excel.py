import sqlite3

from aiogram import types
from aiogram.types import InputFile

from openpyxl import Workbook
from data.config import ADMINS
from loader import dp, dbc, dbcu

sonlar = {
    '0': "0️⃣",
    '1': "1️⃣",
    '2': "2️⃣",
    '3': "3️⃣",
    '4': "4️⃣",
    '5': "5️⃣",
    '6': "6️⃣",
    '7': "7️⃣",
    '8': "8️⃣",
    '9': "9️⃣",
}


@dp.message_handler(text="/allusers", user_id=ADMINS[:])
async def get_all_users(message: types.Message):
    wb = Workbook()

    courses = dbc.select_all_courses()
    for course in courses:
        # ws = wb.active
        ws = wb.create_sheet()
        ws.title = f"{course[2]} ro'yxati"

        SQL_QUERY = "select * from CourseUsers"

        conn = sqlite3.connect('data/course_users.db')
        c = conn.cursor()

        c.execute(SQL_QUERY)

        row = c.fetchall()
        new_list = []
        for course_user in row:
            if course_user[1] == course[2]:
                new_list.append(course_user)

        column_list = []
        for column_name in c.description:
            column_list.append(column_name[0])
        ws.append(column_list)

        for result in new_list:
            ws.append(list(result))

    wb.save("Users.xlsx")
    file = InputFile(path_or_bytesio='Users.xlsx')
    # file = InputFile(path_or_bytesio='test.xlsx')
    count = len(dbcu.select_all_users())
    s = ""
    for i in str(count):
        s += sonlar.get(i, i)

    await message.answer_document(file, caption=f'\n▶️Foydalanuvchilar soni👉    {s}ta\n'
                                                '▶️Ishga tushirilgan vaqti:   <b>22/01/2022</b>\n'
                                                '▶️Dasturchi: @iDekUz')
