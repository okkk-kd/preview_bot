import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dataBase.connection_db import create_connection
from dataBase.execute_query import execute_query

db_name = "clients" + "_bot.db"
db_question = "question.db"
storage = MemoryStorage()

# API_TOKEN = "5287234911:AAHdvM3Wr0mxVaGKmafSSx4TSo4fVSAuOuQ"
API_TOKEN = "5201780383:AAFFrv7H2xhESrX2EN9RA8UjhDkxYXvIa_g"
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)

create_connection(db_name)
create_connection(db_question)

execute_query(db_name, "scripts\create_db_client.sql")
execute_query(db_question, "scripts\create_db_client_copy.sql")