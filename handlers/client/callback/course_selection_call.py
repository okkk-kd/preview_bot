from src.course_sel import course_sellection_kb, \
    course_callback
from src.get_arr import get_arr
from src.course_sel import course_sellection_kb

from aiogram.types import InlineKeyboardButton
from aiogram import types, Dispatcher

import logging

async def cours_page_handler_next(query: types.CallbackQuery, callback_data: dict):
    uni = get_arr("course.txt")
    page = int(callback_data['course_page'])
    current = int(callback_data['course_current'])
    i = current - 3
    print(query.data)
    keyboard = course_sellection_kb("course.txt", page = page, current=current)
    while (i < current):
        if (len(uni) > i):
            keyboard.add(InlineKeyboardButton(uni[i], callback_data="course_" + str(i)))
        else:
            keyboard.add(InlineKeyboardButton("IGNORE", callback_data="IGNORE"))
        i += 1
    logging.info(callback_data)
    await query.message.edit_text("course", reply_markup=keyboard)

async def cours_page_handler_back(query: types.CallbackQuery, callback_data: dict):
    uni = get_arr("course.txt")
    page = int(callback_data['course_page'])
    current = int(callback_data['course_current'])
    print(query.data)
    keyboard = course_sellection_kb("course.txt", page, current)
    i = current - 3
    j = 0
    while (j < 3):
        if (len(uni) > i):
            keyboard.add(InlineKeyboardButton(uni[i], callback_data="course_" + str(i)))
        else:
            keyboard.add(InlineKeyboardButton("IGNORE", callback_data="IGNORE"))
        i += 1
        j += 1
    logging.info(callback_data)
    await query.message.edit_text("course", reply_markup=keyboard)

def register_callback_handlers_course_selection(dp: Dispatcher, state):
    dp.register_callback_query_handler(cours_page_handler_next, course_callback.filter(course_action='course_next'), state=state)
    dp.register_callback_query_handler(cours_page_handler_back, course_callback.filter(course_action='course_back'), state=state)