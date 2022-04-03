from aiogram import Dispatcher, types
from dataBase.execute_query import execute_query, paste_user
from create_bot import db_name

from create_bot import dp, bot
from keyboards import btn_case_admin

#  __________________________старт_____________________________

async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Hello, I was created to introduce you to telegram-bots. If you see this message, you have started a dialogue with me, and here can be any message that you want to show to anyone who starts a dialogue with me\n\nЗдравствуйте, я создан, чтобы познакомить вас с телеграм-ботами. Если вы видите это сообщение, вы начали диалог со мной, и здесь может быть любое сообщение, которое вы хотите показать всем, кто начинает диалог со мной.', reply_markup=btn_case_admin)
    except:
        await message.answer('Something went wrong, error messages are processed by me as quickly as possible\n\nЧто-то пошло не так, сообщения об ошибках обрабатываются мной максимально быстро')



def register_handlers_client(dp: Dispatcher):
    offer=lambda c: c.data.find("Offer") > 0
    dp.register_message_handler(command_start, commands=['load requests'])
    dp.register_message_handler(command_start, commands=['remove requests'])
    dp.register_callback_query_handler(command_start, offer)