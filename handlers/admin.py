from aiogram import Dispatcher, types
from aiohttp import request
from dataBase.execute_query import execute_query, paste_user
from create_bot import db_name
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from dataBase.execute_query import execute_query, paste_user

from create_bot import dp, bot
from keyboards import btn_case_admin, inline_btn_block_control, btn_request_form

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
        await message.answer("Вы авторизованы как админ", reply_markup=btn_case_admin)
    else:
        await message.answer("У вас нет доступа")

async def load_requests(message : types.Message):
    requests = each_el_db()
    length = len(requests)
    i = 0
    print(requests)
    print(length)
    while (i < length):
        await message.answer("Id: " + str(requests[i][0]) + "\nИмя: " + str(requests[i][1]) + "\nТелефон: " + str(requests[i][2]) + "\nNickname: " + str(requests[i][3]) + "\nТариф: " + str(requests[i][6]), reply_markup=inline_btn_block_control)
        i+=1

@dp.callback_query_handler(text_startswith='accept')
async def accept_btn(callback : types.CallbackQuery):
    stmt = callback.message.text
    if (stmt.find("Id:") == 0):
        id = stmt[4]
        query = "UPDATE bot SET status=2 WHERE id ='" + id + "'"
        execute_query(db_name=db_name, query=query)
        await callback.answer()


def each_el_db():
    requests : list = []
    stmt = "SELECT * FROM bot WHERE status = 1"
    requests.append(execute_query(db_name=db_name, query=stmt))
    return execute_query(db_name=db_name, query=stmt)
    

async def remove_requests(message : types.Message):
    requests = each_el_db_r()
    length = len(requests)
    i = 0
    print(requests)
    print(length)
    while (i < length):
        await message.answer("Id: " + str(requests[i][0]) + "\nИмя: " + str(requests[i][1]) + "\nТелефон: " + str(requests[i][2]) + "\nNickname: " + str(requests[i][3]) + "\nТариф: " + str(requests[i][6]), reply_markup=inline_btn_block_control)
        i+=1

def each_el_db_r():
    requests : list = []
    stmt = "SELECT * FROM bot WHERE status != 1"
    requests.append(execute_query(db_name=db_name, query=stmt))
    return execute_query(db_name=db_name, query=stmt)

@dp.callback_query_handler(text_startswith='profile')
async def get_profile(callback : types.CallbackQuery):
    stmt = callback.message.text
    if (stmt.find("Id:") == 0):
        id = stmt[4]
        query = "SELECT * FROM bot WHERE id = '" + id + "'"
        nick_name = execute_query(db_name=db_name, query=query)
    await bot.send_message(callback.from_user.id, "https://t.me/" + nick_name[0][3])
    await callback.answer()

@dp.callback_query_handler(text_startswith='invite')
async def get_profile(callback : types.CallbackQuery):
    stmt = callback.message.text
    if (stmt.find("Id:") == 0):
        id = stmt[4]
        query = "SELECT * FROM bot WHERE id = '" + id + "'"
        nick_name = execute_query(db_name=db_name, query=query)
    await bot.send_message(int(nick_name[0][4]), "https://t.me/+LLZVEmKsmmYwNWUy")
    await callback.answer()

async def old_keyboard(message : types.Message):
    await message.answer("Вы вернули стандартную клавиатуру", reply_markup=btn_request_form)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(load_requests, commands=['активные_заявки'])
    dp.register_message_handler(old_keyboard, commands=['вернуть_прежнюю_клавиатуру'])
    dp.register_message_handler(remove_requests, commands=['неактивные_заявки'])
    dp.register_message_handler(auth_admin, commands=['авторизация'])