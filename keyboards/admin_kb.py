from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

btn_load_requests = KeyboardButton('/load_requests')
btn_remove_requests = KeyboardButton('/remove_requests')

btn_case_admin = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(btn_load_requests)\
    .insert(btn_remove_requests)


inline_btn_accept = InlineKeyboardButton('accept', callback_data='accept')
inline_btn_1_profile = InlineKeyboardButton('profile', callback_data='profile')
inline_btn_2_invite = InlineKeyboardButton('invite', callback_data='invite')
inline_btn_block_control = InlineKeyboardMarkup(row_width=2)\
    .add(inline_btn_accept)\
    .insert(inline_btn_1_profile)\
    .add(inline_btn_2_invite)