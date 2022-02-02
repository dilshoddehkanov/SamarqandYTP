from aiogram import executor

from loader import dp, dbc, dbu, dbcu, dbs
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Ma'lumotlar bazasini yaratamiz:
    try:
        dbc.create_table_courses()
        dbs.create_table_services()
        dbcu.create_table_courseusers()
        dbu.create_table_users()
    except Exception as err:
        print(err)



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
