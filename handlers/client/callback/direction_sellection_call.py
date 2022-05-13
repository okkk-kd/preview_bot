from src.dir_sel import get_arr_dir, \
    dir_sellection_kb, \
    dir_callback
from src.parse_digit import parse_digit

from create_bot import dp

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

import logging

async def dir_page_handler_next(query: types.CallbackQuery, callback_data: dict):
    uni = get_arr_dir("direction.txt")
    page = int(callback_data['dir_page'])
    current = int(callback_data['dir_current'])
    i = current - 3
    print(query.data)
    keyboard = dir_sellection_kb("direction.txt", page = page, current=current)
    while (i < current):
        if (len(uni) > i):
            keyboard.add(InlineKeyboardButton(uni[i], callback_data="dir_" + str(i)))
        else:
            keyboard.add(InlineKeyboardButton("IGNORE", callback_data="IGNORE"))
        i += 1
    logging.info(callback_data)
    await query.message.edit_text("dir", reply_markup=keyboard)

async def dir_page_handler_back(query: types.CallbackQuery, callback_data: dict):
    uni = get_arr_dir("direction.txt")
    page = int(callback_data['dir_page'])
    current = int(callback_data['dir_current'])
    print(query.data)
    keyboard = dir_sellection_kb("direction.txt", page, current)
    i = current - 3
    j = 0
    while (j < 3):
        if (len(uni) > i):
            keyboard.add(InlineKeyboardButton(uni[i], callback_data="dir_" + str(i)))
        else:
            keyboard.add(InlineKeyboardButton("IGNORE", callback_data="IGNORE"))
        i += 1
        j += 1
    logging.info(callback_data)
    await query.message.edit_text("dir", reply_markup=keyboard)

async def dir_button_select(query: types.CallbackQuery, state: FSMContext):
    if (len(get_arr_dir("direction.txt")) > parse_digit(query.data)):
        await state.update_data(uni=get_arr_dir("direction.txt")[parse_digit(query.data)])
        print(get_arr_dir("direction.txt")[parse_digit(query.data)])


def register_callback_handlers_dir_selection(dp: Dispatcher, state):
    dir_pages=lambda c: c.data.startswith("dir_")
    dp.register_callback_query_handler(dir_page_handler_next, dir_callback.filter(dir_action='dir_next'), state=state)
    dp.register_callback_query_handler(dir_page_handler_back, dir_callback.filter(dir_action='dir_back'), state=state)
    dp.register_callback_query_handler(dir_button_select, dir_pages, state=state)