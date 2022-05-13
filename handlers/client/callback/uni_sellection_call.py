from src.uni_sel import get_arr_uni, \
    uni_sellection_kb, \
    uni_callback
from src.parse_digit import parse_digit

from create_bot import dp

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

import logging

async def uni_page_handler_next(query: types.CallbackQuery, callback_data: dict):
    uni = get_arr_uni("uni.txt")
    page = int(callback_data['page'])
    current = int(callback_data['current'])
    i = current - 3
    print(page, current)
    keyboard = uni_sellection_kb("uni.txt", page = page, current=current)
    while (i < current):
        if (len(uni) > i):
            keyboard.add(InlineKeyboardButton(uni[i], callback_data="uni_" + str(i)))
        else:
            keyboard.add(InlineKeyboardButton("IGNORE", callback_data="IGNORE"))
        i += 1
    logging.info(callback_data)
    await query.message.edit_text("LLLL", reply_markup=keyboard)

async def uni_page_handler_back(query: types.CallbackQuery, callback_data: dict):
    uni = get_arr_uni("uni.txt")
    page = int(callback_data['page'])
    current = int(callback_data['current'])
    keyboard = uni_sellection_kb("uni.txt", page, current)
    i = current - 3
    j = 0
    print(page, current)
    while (j < 3):
        if (len(uni) > i):
            keyboard.add(InlineKeyboardButton(uni[i], callback_data="uni_" + str(i)))
        else:
            keyboard.add(InlineKeyboardButton("IGNORE", callback_data="IGNORE"))
        i += 1
        j += 1
    logging.info(callback_data)
    await query.message.edit_text("LLLL", reply_markup=keyboard)

def register_callback_handlers_uni_selection(dp: Dispatcher, state):
    dp.register_callback_query_handler(uni_page_handler_next, uni_callback.filter(action='next'), state=state)
    dp.register_callback_query_handler(uni_page_handler_back, uni_callback.filter(action='back'), state=state)
