from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from src.dir_sel import dir_sellection_kb
from src.uni_sel import uni_sellection_kb
#  __________________________основная клавиатура_____________________________

btn_start = KeyboardButton('/заявка') # ok
btn_cancel = KeyboardButton('/отмена') # ok
btn_info = KeyboardButton('/информация') # ok
btn_auth = KeyboardButton('/авторизация') # ok
btn_request_form = ReplyKeyboardMarkup(resize_keyboard=True)
btn_request_form\
    .add(btn_start)\
    .insert(btn_cancel)\
    .add(btn_info)\
    .add(btn_auth)\

#  __________________________FAQ клавиатура_____________________________

inline_btn_FAQ = InlineKeyboardButton('FAQ', callback_data='FAQ')
inline_btn_about = InlineKeyboardButton('о занятиях', callback_data='about')
inline_btn_block_info = InlineKeyboardMarkup(row_width=2)\
    .add(inline_btn_FAQ)\
    .insert(inline_btn_about)

#  __________________________FAQ вопросы_________________________________

inline_btn_1_q = InlineKeyboardButton('Что-то', callback_data='1_q')
inline_btn_2_q = InlineKeyboardButton('Или', callback_data='2_q')
inline_btn_3_q = InlineKeyboardButton('Часто', callback_data='3_q')
inline_btn_4_q = InlineKeyboardButton('Задаваемые', callback_data='4_q')
inline_btn_5_q = InlineKeyboardButton('Вопросы', callback_data='5_q')
inline_btn_new_q = InlineKeyboardButton('Задать новый вопрос', callback_data='new_q')
inline_btn_block_q = InlineKeyboardMarkup(row_width=1)\
    .add(inline_btn_1_q)\
    .add(inline_btn_2_q)\
    .add(inline_btn_3_q)\
    .add(inline_btn_4_q)\
    .add(inline_btn_5_q)\
    .add(inline_btn_new_q)

# _________________ Inline кнопки отправки вопроса ________________________

btn_cancel_q = KeyboardButton("/отмена_вопроса")
btn_cancel_new_question = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_cancel_q)

# __________________________ Выбор университета ___________________________

btn_uni_select_kb = uni_sellection_kb("uni.txt")

# __________________________ Выбор университета ___________________________

btn_dir_select_kb = dir_sellection_kb("direction.txt")