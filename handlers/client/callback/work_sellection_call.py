from src.work_sel import work_sellection_kb, \
    work_callback
from src.get_arr import get_arr

from aiogram.types import InlineKeyboardButton
from aiogram import types, Dispatcher

import logging

async def work_page_handler_next(query: types.CallbackQuery, callback_data: dict):
    work = get_arr("type_of_work.txt")
    page = int(callback_data['work_page'])
    current = int(callback_data['work_current'])
    i = current - 3
    print(query.data)
    keyboard = work_sellection_kb("type_of_work.txt", page = page, current=current)
    while (i < current):
        if (len(work) > i):
            keyboard.add(InlineKeyboardButton(work[i], callback_data="work_" + str(i)))
        else:
            keyboard.add(InlineKeyboardButton("IGNORE", callback_data="IGNORE"))
        i += 1
    logging.info(callback_data)
    await query.message.edit_text("work", reply_markup=keyboard)

async def work_page_handler_back(query: types.CallbackQuery, callback_data: dict):
    work = get_arr("type_of_work.txt")
    page = int(callback_data['work_page'])
    current = int(callback_data['work_current'])
    print(query.data)
    keyboard = work_sellection_kb("type_of_work.txt", page, current)
    i = current - 3
    j = 0
    while (j < 3):
        if (len(work) > i):
            keyboard.add(InlineKeyboardButton(work[i], callback_data="work_" + str(i)))
        else:
            keyboard.add(InlineKeyboardButton("IGNORE", callback_data="IGNORE"))
        i += 1
        j += 1
    logging.info(callback_data)
    await query.message.edit_text("work", reply_markup=keyboard)

def register_callback_handlers_work_selection(dp: Dispatcher, state):
    dp.register_callback_query_handler(work_page_handler_next, work_callback.filter(work_action='work_next'), state=state)
    dp.register_callback_query_handler(work_page_handler_back, work_callback.filter(work_action='work_back'), state=state)