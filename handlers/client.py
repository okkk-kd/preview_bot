from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from dataBase.execute_query import execute_query, paste_user
from create_bot import db_name
import aiogram.utils.markdown as md
from aiogram.types import ParseMode
from dataBase.execute_query import paste_user

from create_bot import dp, bot
from keyboards import btn_request_form

class Form(StatesGroup):
    name = State()
    phone = State()
    nickname = State()
    tg_id = State()
    status = State()

#  __________________________старт_____________________________

async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Hello, I was created to introduce you to telegram-bots. If you see this message, you have started a dialogue with me, and here can be any message that you want to show to anyone who starts a dialogue with me\n\nЗдравствуйте, я создан, чтобы познакомить вас с телеграм-ботами. Если вы видите это сообщение, вы начали диалог со мной, и здесь может быть любое сообщение, которое вы хотите показать всем, кто начинает диалог со мной.', reply_markup=btn_request_form)
    except:
        await message.answer('Something went wrong, error messages are processed by me as quickly as possible\n\nЧто-то пошло не так, сообщения об ошибках обрабатываются мной максимально быстро')

def check_username(userid):
    id = execute_query(db_name, "SELECT EXISTS(SELECT tg_id FROM bot WHERE tg_id = '" + str(userid) + "' AND status = 1)")
    print("id: " + str(id))
    return id

#  __________________________форма_____________________________

async def user_form_start(message : types.Message):
    try:
        print (message.from_user.id)
        print (message.from_user.first_name)
        print (message.from_user.last_name)
        if (check_username(message.from_user.id)[0][0] == 1):
            await message.answer('Your application is being processed, please wait for a response\n\nВаша заявка обрабатывается, дождитесь ответа')
        else:
            await Form.name.set()
            await message.answer('Enter your name\n\nВведие ваше имя')
    except:
        await message.answer('Something went wrong, error messages are processed by me as quickly as possible\n\nЧто-то пошло не так, сообщения об ошибках обрабатываются мной максимально быстро')

async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('Cancellation was successful\n\nОтмена произошла успешно')

async def get_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        data['tg_id'] = message.from_user.id
        data['nickname'] = message.from_user.username
        data['status'] = 1
    await Form.next()
    await message.answer('Enter phone number\n\nВведите номер телефона')

async def get_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    user = [
        (data['name'],
        data['phone'],
        data['tg_id'],
        data['nickname'],
        data['status'])
    ]
    condition = lambda a : "Обрабатывается | being processed" if (a == 1) else "Ошибка | Error status"
    await bot.send_message(
            
            message.chat.id,
            md.text(
                md.text('Имя: ', data['name']),
                md.text('Телефон: ', data['phone']),
                md.text('Telegram id: ', data['tg_id']),
                md.text('Имя пользователя: ', data['nickname']),
                md.text('Статус: ', condition(data['status'])),
                sep='\n',
            ),
            parse_mode=ParseMode.MARKDOWN,
        )
    paste_user(db_name, user)
    await state.finish()

#  __________________________инфо_____________________________

async def command_info(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Any of your information can be located here, you can see an example for yourself:\n\nЗдесь может располагаться любая ваша информация, пример вы можете видеть сами:', reply_markup=btn_request_form)
    except:
        await message.answer('Something went wrong, error messages are processed by me as quickly as possible\n\nЧто-то пошло не так, сообщения об ошибках обрабатываются мной максимально быстро')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'старт'])
    dp.register_message_handler(command_info, commands=['инфо'])
    dp.register_message_handler(user_form_start, commands=['заявка'])
    dp.register_message_handler(cancel_handler, commands=['отмена'], state='*')
    dp.register_message_handler(get_name, state=Form.name)
    dp.register_message_handler(get_phone, state=Form.phone)