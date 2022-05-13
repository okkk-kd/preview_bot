from aiogram import types, Dispatcher

from keyboards.request import btn_request_form

from create_bot import bot, dp

async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Здравствуйте, я создан, чтобы познакомить вас с телеграм-ботами. Если вы видите это сообщение, вы начали диалог со мной, и здесь может быть любое сообщение, которое вы хотите показать всем, кто начинает диалог со мной.\nДля получения доступа к управлению заявками намипишите мне: https://t.me/kritinidzin', reply_markup=btn_request_form)
    except:
        await message.answer('Что-то пошло не так, сообщения об ошибках обрабатываются мной максимально быстро')

def register_handlers_start(dp: Dispatcher):
        dp.register_message_handler(command_start, commands=['start', 'старт'])