from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_load_requests = KeyboardButton('/load requests')
btn_remove_requests = KeyboardButton('/remove requests')

btn_case_admin = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(btn_load_requests)\
    .insert(btn_remove_requests)
