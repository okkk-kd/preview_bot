from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram import types

def get_arr_uni(path_fie):
    file = open(path_fie, 'rb')
    line = file.readline().decode('utf-8')
    uni = []
    while (line):
        uni.append(line)
        line = file.readline().decode('utf-8')
    return uni

uni_callback = CallbackData("uni", "page", "action", "current")

def uni_sellection_kb(path, page: int = 0, current: int = 3) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=3)
    uni = get_arr_uni(path)
    has_next_page = len(uni) > page + 1
    if page != 0:
        keyboard.insert(
            InlineKeyboardButton(
                text="< Назад",
                callback_data=uni_callback.new(action='back', page=page - 1, current=current - 3)
            )
        )
    keyboard.insert(
        InlineKeyboardButton(
            text=f"• {page + 1}",
            callback_data="dont_click_me"
        )
    )
    if has_next_page:
        keyboard.insert(
            InlineKeyboardButton(
                text="Вперёд >",
                callback_data=uni_callback.new(action='next', page=page + 1, current=current + 3)
            )
        )
    return keyboard