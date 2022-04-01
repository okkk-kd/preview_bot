from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import keyboards as kb
from aiogram import Dispatcher, types

btn_start = KeyboardButton('/заявка') # ok
btn_cancel = KeyboardButton('/отмена') # ok
btn_info = KeyboardButton('/инфо')
btn_schedule = KeyboardButton('/расписание')
btn_tariffs = KeyboardButton('/тарифы')
btn_request_form = ReplyKeyboardMarkup(resize_keyboard=True)
btn_request_form.add(btn_start).insert(btn_cancel).add(btn_schedule).insert(btn_info).add(btn_tariffs)

async def process_start_command(message: types.Message):
    await message.answer("Привет!", reply_markup=btn_request_form)