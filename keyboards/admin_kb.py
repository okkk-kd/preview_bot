from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

btn_load_requests = KeyboardButton('/активные_заявки')
btn_remove_requests = KeyboardButton('/неактивные_заявки')
btn_standart_kb = KeyboardButton('/вернуть_прежнюю_клавиатуру')
btn_accept_q = KeyboardButton('/просмотр_новых_вопросов')

btn_case_admin = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(btn_load_requests)\
    .insert(btn_remove_requests)\
    .add(btn_accept_q)\
    .add(btn_standart_kb)


inline_btn_accept = InlineKeyboardButton('Принять', callback_data='accept')
inline_btn_1_profile = InlineKeyboardButton('Профиль', callback_data='profile')
inline_btn_2_invite = InlineKeyboardButton('Приглашение в группу', callback_data='invite')
inline_btn_block_control = InlineKeyboardMarkup(row_width=2)\
    .add(inline_btn_accept)\
    .insert(inline_btn_1_profile)\
    .add(inline_btn_2_invite)