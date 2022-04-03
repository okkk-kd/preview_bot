from aiogram import Dispatcher, types
from dataBase.execute_query import execute_query, paste_user
from create_bot import db_name
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from create_bot import dp, bot
from keyboards import btn_case_admin, inline_btn_block_control

class auth_adm(StatesGroup):
    id = State()

#  __________________________старт_____________________________

# async def command_start(message : types.Message):
#     try:
#         await bot.send_message(message.from_user.id, 'Hello, I was created to introduce you to telegram-bots. If you see this message, you have started a dialogue with me, and here can be any message that you want to show to anyone who starts a dialogue with me\n\nЗдравствуйте, я создан, чтобы познакомить вас с телеграм-ботами. Если вы видите это сообщение, вы начали диалог со мной, и здесь может быть любое сообщение, которое вы хотите показать всем, кто начинает диалог со мной.', reply_markup=btn_case_admin)
#     except:
#         await message.answer('Something went wrong, error messages are processed by me as quickly as possible\n\nЧто-то пошло не так, сообщения об ошибках обрабатываются мной максимально быстро')
async def auth_admin(message : types.Message):
    if (message.from_user.id == 995404025):
        await message.answer("admin auth", reply_markup=btn_case_admin)

async def load_requests(message : types.Message):
    await message.answer("Load method", reply_markup=inline_btn_block_control)

async def remove_requests(message : types.Message):
    await message.answer("Remove method")

def register_handlers_admin(dp: Dispatcher):
    offer=lambda c: c.data.find("Offer") > 0
    dp.register_message_handler(load_requests, commands=['load_requests'])
    dp.register_message_handler(remove_requests, commands=['remove_requests'])
    dp.register_message_handler(auth_admin, commands=['auth'])