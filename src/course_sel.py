from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from src.get_arr import get_arr

course_callback = CallbackData("course", "course_page", "course_action", "course_current")

def course_sellection_kb(path, page: int = 0, current: int = 3) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=3)
    uni = get_arr(path)
    has_next_page = len(uni) > page + 1
    if page != 0:
        keyboard.insert(
            InlineKeyboardButton(
                text="< Назад",
                callback_data=course_callback.new(course_action='course_back', course_page=page - 1, course_current=current - 3)
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
                callback_data=course_callback.new(course_action='course_next', course_page=page + 1, course_current=current + 3)
            )
        )
    return keyboard