from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

btn_load_requests = KeyboardButton('/активные_заявки')
btn_remove_requests = KeyboardButton('/неактивные_заявки')
btn_standart_kb = KeyboardButton('/вернуть_прежнюю_клавиатуру')
btn_new_q = KeyboardButton('/новые_вопросы')
btn_accepted_q = KeyboardButton('/старые_вопросы')

btn_case_admin = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(btn_load_requests)\
    .insert(btn_remove_requests)\
    .add(btn_new_q)\
    .insert(btn_accepted_q)\
    .add(btn_standart_kb)


inline_btn_accept = InlineKeyboardButton('Принять', callback_data='accept')
inline_btn_1_profile = InlineKeyboardButton('Профиль', callback_data='profile')
inline_btn_2_invite = InlineKeyboardButton('Приглашение в группу', callback_data='invite')
inline_btn_block_control = InlineKeyboardMarkup(row_width=2)\
    .add(inline_btn_accept)\
    .insert(inline_btn_1_profile)\
    .add(inline_btn_2_invite)

inline_btn_accept = InlineKeyboardButton('Отменить', callback_data='cancle')
inline_btn_1_profile = InlineKeyboardButton('Профиль', callback_data='profile')
inline_btn_2_invite = InlineKeyboardButton('Приглашение в группу', callback_data='invite')
inline_btn_block_control_accepted = InlineKeyboardMarkup(row_width=2)\
    .add(inline_btn_accept)\
    .insert(inline_btn_1_profile)\
    .add(inline_btn_2_invite)

inline_btn_accept_q = InlineKeyboardButton('Принять', callback_data='q_accept')
inline_btn_1_profile_q = InlineKeyboardButton('Профиль', callback_data='q_profile')
inline_btn_block_control_questions = InlineKeyboardMarkup(row_width=2)\
    .add(inline_btn_accept_q)\
    .insert(inline_btn_1_profile_q)

inline_btn_1_profile_q = InlineKeyboardButton('Профиль', callback_data='q_profile')
inline_btn_block_control_questions_old = InlineKeyboardMarkup(row_width=1)\
    .add(inline_btn_1_profile_q)

