from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils.db_api.course_users import Course_users
from utils.db_api.courses import Courses_db
from utils.db_api.service import Services_db
from utils.db_api.sqlite import Database
from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dbu = Database(path_to_db="data/main.db")
dbc = Courses_db(path_to_db='data/courses.db')
dbcu = Course_users(path_to_db='data/course_users.db')
dbs = Services_db(path_to_db='data/services.db')

