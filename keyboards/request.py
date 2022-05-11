from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from algorithms.uni_sel import uni_sellection_kb
#  __________________________основная клавиатура_____________________________

btn_start = KeyboardButton('/заявка') # ok
btn_cancel = KeyboardButton('/отмена_заявки') # ok
btn_info = KeyboardButton('/информация') # ok
btn_schedule = KeyboardButton('/расписание') # ok
btn_tariffs = KeyboardButton('/тарифы') # ok
btn_auth = KeyboardButton('/авторизация') # ok
btn_uni = KeyboardButton('/uni')
btn_request_form = ReplyKeyboardMarkup(resize_keyboard=True)
btn_request_form\
    .add(btn_start)\
    .insert(btn_cancel)\
    .add(btn_schedule)\
    .insert(btn_info)\
    .add(btn_tariffs)\
    .add(btn_auth)\
    .insert(btn_uni)

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

#  __________________________Inline Тариф клавиатура_____________________________

inline_btn_free = InlineKeyboardButton('Бесплатно', callback_data='1 Offer')
inline_btn_1_each_week = InlineKeyboardButton('40$', callback_data='2 Offer')
inline_btn_2_each_week = InlineKeyboardButton('80$', callback_data='3 Offer')
inline_btn_month = InlineKeyboardButton('200$', callback_data='4 Offer')
inline_btn_block_tariffs = InlineKeyboardMarkup(row_width=1)\
    .add(inline_btn_free)\
    .add(inline_btn_1_each_week)\
    .add(inline_btn_2_each_week)\
    .add(inline_btn_month)

inline_btn_request_tariff = InlineKeyboardMarkup(row_width=1)\
    .add(InlineKeyboardButton('Отправить заявку', callback_data='send_request'))

#  __________________________Тариф клавиатура_____________________________

btn_free = KeyboardButton('Бесплатно')
btn_1_each_week = KeyboardButton('40$')
btn_2_each_week = KeyboardButton('80$')
btn_month = KeyboardButton('200$')
btn_block_tariffs = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(btn_free)\
    .add(btn_1_each_week)\
    .add(btn_2_each_week)\
    .add(btn_month)

# _________________ Inline кнопки отправки вопроса ________________________

btn_cancel_q = KeyboardButton("/отмена_вопроса")
btn_cancel_new_question = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_cancel_q)

# __________________________ Выбор университета ___________________________

btn_uni_select_kb = uni_sellection_kb("uni.txt")

