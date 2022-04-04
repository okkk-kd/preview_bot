import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dataBase.connection_db import create_connection
from dataBase.execute_query import execute_query

db_name = "clients" + "_bot.db"
storage = MemoryStorage()

API_TOKEN = "5176755732:AAGIJK5REu4wPnfBbI-VMm84R1wl9X8QTRs"
logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)

create_connection(db_name)

execute_query(db_name, "scripts\create_db.sql")