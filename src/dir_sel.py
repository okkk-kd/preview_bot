from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram import types

def get_arr_dir(path_fie):
    file = open(path_fie, 'rb')
    line = file.readline().decode('utf-8')
    uni = []
    while (line):
        uni.append(line)
        line = file.readline().decode('utf-8')
    return uni

dir_callback = CallbackData("dir", "dir_page", "dir_action", "dir_current")

def dir_sellection_kb(path, page: int = 0, current: int = 3) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=3)
    uni = get_arr_dir(path)
    has_next_page = len(uni) > page + 1
    if page != 0:
        keyboard.insert(
            InlineKeyboardButton(
                text="< Назад",
                callback_data=dir_callback.new(dir_action='dir_back', dir_page=page - 1, dir_current=current - 3)
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
                callback_data=dir_callback.new(dir_action='dir_next', dir_page=page + 1, dir_current=current + 3)
            )
        )
    return keyboard