from aiogram import Dispatcher, types
from aiohttp import request
from dataBase.execute_query import execute_query, paste_user
from create_bot import db_name, db_question
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from dataBase.execute_query import execute_query, paste_user

from create_bot import dp, bot
from keyboards import btn_case_admin, inline_btn_block_control, btn_request_form, inline_btn_block_control_accepted, inline_btn_block_control_questions, inline_btn_block_control_questions_old

async def auth_admin(message : types.Message):
    await message.answer("Вы авторизованы как админ", reply_markup=btn_case_admin)

async def load_requests(message : types.Message):
    requests = each_el_db()
    length = len(requests)
    i = 0
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
        await callback.message.delete()


def each_el_db():
    requests : list = []
    stmt = "SELECT * FROM bot WHERE status = 1"
    requests.append(execute_query(db_name=db_name, query=stmt))
    return execute_query(db_name=db_name, query=stmt)
    

async def remove_requests(message : types.Message):
    requests = each_el_db_r()
    length = len(requests)
    i = 0
    while (i < length):
        await message.answer("Id: " + str(requests[i][0]) + "\nИмя: " + str(requests[i][1]) + "\nТелефон: " + str(requests[i][2]) + "\nNickname: " + str(requests[i][3]) + "\nТариф: " + str(requests[i][6]), reply_markup=inline_btn_block_control_accepted)
        i+=1

def each_el_db_r():
    stmt = "SELECT * FROM bot WHERE status != 1"
    return execute_query(db_name=db_name, query=stmt)

@dp.callback_query_handler(text_startswith='cancle')
async def accept_btn(callback : types.CallbackQuery):
    stmt = callback.message.text
    if (stmt.find("Id:") == 0):
        id = stmt[4]
        query = "UPDATE bot SET status=1 WHERE id ='" + id + "'"
        execute_query(db_name=db_name, query=query)
        await callback.message.delete()
        await callback.answer()

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


async def get_questions_new(message : types.Message):
    requests = each_el_db_questions()
    length = len(requests)
    i = 0
    while (i < length):
        await message.answer("Id: " + str(requests[i][0]) + "\nNickname: " + str(requests[i][1]) + "\nВопрос: " + str(requests[i][4]), reply_markup=inline_btn_block_control_questions)
        i+=1

def each_el_db_questions():
    requests : list = []
    stmt = "SELECT * FROM question WHERE status == 1"
    return execute_query(db_name=db_question, query=stmt)

@dp.callback_query_handler(text_startswith='q_accept')
async def accept_btn_q(callback : types.CallbackQuery):
    stmt = callback.message.text
    if (stmt.find("Id:") == 0):
        id = stmt[4]
        print(id)
        query = "UPDATE question SET status=2 WHERE id =='" + id + "'"
        execute_query(db_name=db_question, query=query)
        await callback.answer()
        await callback.message.delete()

async def get_questions_old(message : types.Message):
    requests = each_el_db_questions_old()
    length = len(requests)
    i = 0
    while (i < length):
        await message.answer("Id: " + str(requests[i][0]) + "\nNickname: " + str(requests[i][1]) + "\nВопрос: " + str(requests[i][4]), reply_markup=inline_btn_block_control_questions_old)
        i+=1

def each_el_db_questions_old():
    stmt = "SELECT * FROM question WHERE status != 1"
    return execute_query(db_name=db_question, query=stmt)

@dp.callback_query_handler(text_startswith='q_cancle')
async def accept_btn_q(callback : types.CallbackQuery):
    stmt = callback.message.text
    if (stmt.find("Id:") == 0):
        id = stmt[4]
        print(id)
        query = "UPDATE question SET status=1 WHERE id =='" + id + "'"
        execute_query(db_name=db_question, query=query)
        await callback.answer()
        await callback.message.delete()

@dp.callback_query_handler(text_startswith='q_profile')
async def get_profile(callback : types.CallbackQuery):
    stmt = callback.message.text
    if (stmt.find("Id:") == 0):
        id = stmt[4]
        query = "SELECT * FROM question WHERE id = '" + id + "'"
        nick_name = execute_query(db_name=db_question, query=query)
    await bot.send_message(callback.from_user.id, "https://t.me/" + nick_name[0][2])
    await callback.answer()

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(load_requests, commands=['активные_заявки'])
    dp.register_message_handler(old_keyboard, commands=['вернуть_прежнюю_клавиатуру'])
    dp.register_message_handler(remove_requests, commands=['неактивные_заявки'])
    dp.register_message_handler(auth_admin, commands=['авторизация'])
    dp.register_message_handler(get_questions_new, commands=['новые_вопросы'])
    dp.register_message_handler(get_questions_old, commands=['старые_вопросы'])