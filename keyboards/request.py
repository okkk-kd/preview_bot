from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import keyboards as kb
from aiogram import Dispatcher, types

btn_start = KeyboardButton('/request') # ok
btn_cancel = KeyboardButton('/cancell') # ok
btn_info = KeyboardButton('/info') # ok
btn_schedule = KeyboardButton('/schedule') # ok
btn_tariffs = KeyboardButton('/tariffs') # ok
btn_request_form = ReplyKeyboardMarkup(resize_keyboard=True)
btn_request_form\
    .add(btn_start)\
    .insert(btn_cancel)\
    .add(btn_schedule)\
    .insert(btn_info)\
    .add(btn_tariffs)

inline_btn_FAQ = InlineKeyboardButton('FAQ', callback_data='FAQ')
inline_btn_about = InlineKeyboardButton('about', callback_data='about')
inline_btn_block_info = InlineKeyboardMarkup(row_width=2)\
    .add(inline_btn_FAQ)\
    .insert(inline_btn_about)

# inline_btn_free = InlineKeyboardButton('1 Offer | 1 Предложение', callback_data='1 Offer')
# inline_btn_1_each_week = InlineKeyboardButton('2 Offer | 2 Предложение', callback_data='2 Offer')
# inline_btn_2_each_week = InlineKeyboardButton('3 Offer | 3 Предложение', callback_data='3 Offer')
# inline_btn_month = InlineKeyboardButton('4 Offer | 4 Предложение', callback_data='4 Offer')
# inline_btn_block_tariffs = InlineKeyboardMarkup(row_width=1)\
#     .add(inline_btn_free)\
#     .add(inline_btn_1_each_week)\
#     .add(inline_btn_2_each_week)\
#     .add(inline_btn_month)

btn_free = KeyboardButton('1 Offer | 1 Предложение')
btn_1_each_week = KeyboardButton('2 Offer | 2 Предложение')
btn_2_each_week = KeyboardButton('3 Offer | 3 Предложение')
btn_month = KeyboardButton('4 Offer | 4 Предложение')
btn_block_tariffs = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(btn_free)\
    .add(btn_1_each_week)\
    .add(btn_2_each_week)\
    .add(btn_month)