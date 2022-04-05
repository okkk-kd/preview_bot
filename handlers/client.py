from subprocess import call
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from dataBase.execute_query import execute_query, paste_user
from create_bot import db_name
import aiogram.utils.markdown as md
from aiogram.types import ParseMode
import logging

from create_bot import dp, bot
from keyboards import btn_request_form, inline_btn_block_info, btn_block_tariffs, inline_btn_block_tariffs, inline_btn_block_q, inline_btn_request_tariff
from schedule.schedule import return_schedule, Schedule_ob

class Form(StatesGroup):
    name = State()
    tariff = State()
    phone = State()
    nickname = State()
    tg_id = State()
    status = State()

#  __________________________старт_____________________________

async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Hello, I was created to introduce you to telegram-bots. If you see this message, you have started a dialogue with me, and here can be any message that you want to show to anyone who starts a dialogue with me\n\nЗдравствуйте, я создан, чтобы познакомить вас с телеграм-ботами. Если вы видите это сообщение, вы начали диалог со мной, и здесь может быть любое сообщение, которое вы хотите показать всем, кто начинает диалог со мной.\nДля получения доступа к управлению заявками намипишите мне: https://t.me/kritinidzin', reply_markup=btn_request_form)
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

async def cancel_handler(message: types.Message, state: Form):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('Cancellation was successful\n\nОтмена произошла успешно')

async def get_name(message: types.Message, state: Form):
    async with state.proxy() as data:
        data['name'] = message.text
        data['tg_id'] = message.from_user.id
        data['nickname'] = message.from_user.username
        data['status'] = 1
    await Form.next()
    await message.answer('Choose a plan | Выберите тариф', reply_markup=btn_block_tariffs)

async def get_tariff_form(message: types.Message, state: Form):
    async with state.proxy() as data:
        data['tariff'] = message.text
    await Form.next()
    await message.answer('Введите телефон', reply_markup=btn_request_form)

async def get_phone(message: types.Message, state: Form):
    async with state.proxy() as data:
        data['phone'] = message.text
    user = [
        (data['name'],
        data['phone'],
        data['tg_id'],
        data['nickname'],
        data['status'],
        data['tariff'])
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
                md.text('Тариф: ', data['tariff']),
                sep='\n',
            ),
            parse_mode=ParseMode.MARKDOWN,
        )
    paste_user(db_name, user)
    await state.finish()

#  __________________________инфо_____________________________

async def command_info(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Any of your information can be located here, you can see an example for yourself:\n\nЗдесь может располагаться любая ваша информация, пример вы можете видеть сами:', reply_markup=inline_btn_block_info)
    except:
        await message.answer('Something went wrong, error messages are processed by me as quickly as possible\n\nЧто-то пошло не так, сообщения об ошибках обрабатываются мной максимально быстро')

async def info_FAQ(callback : types.CallbackQuery):
    await callback.message.answer("Here you can find answers to frequently asked questions\n\nЗдесь вы модете найти ответ на часто задаваемые вопросы", reply_markup=inline_btn_block_q)
    await callback.answer()

async def info_about(callback : types.CallbackQuery):
    await callback.message.answer(callback.data)
    await callback.answer()

async def info_questions(callback : types.CallbackQuery):
    match callback.data:
        case "1_q":
            await callback.message.answer("Answer to the 1_q question")
            await callback.answer()
        case "2_q":
            await callback.message.answer("Answer to the 2_q question")
            await callback.answer()
        case "3_q":
            await callback.message.answer("Answer to the 3_q question")
            await callback.answer()
        case "4_q":
            await callback.message.answer("Answer to the 4_q question")
            await callback.answer()
        case "5_q":
            await callback.message.answer("Answer to the 5_q question")
            await callback.answer()
        case "new_q":
            await callback.message.answer("Answer to the new_q question")
            await callback.answer()

#  __________________________тарифы_____________________________

async def tariffs_info(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Any payment related information can be found here.\n\nЗдесь может находиться любая информация касающаяся оплаты', reply_markup=inline_btn_block_tariffs)
    except:
        await message.answer('Something went wrong, error messages are processed by me as quickly as possible\n\nЧто-то пошло не так, сообщения об ошибках обрабатываются мной максимально быстро')

async def send_offer_prewiew(callback : types.CallbackQuery):
    match callback.data:
        case "1 Offer":
            await callback.message.answer('Дополнительная информация о данном тарифе 1', reply_markup=inline_btn_request_tariff)
            await callback.answer()
        case "2 Offer":
            await callback.message.answer('Дополнительная информация о данном тарифе 2', reply_markup=inline_btn_request_tariff)
            await callback.answer()
        case "3 Offer":
            await callback.message.answer('Дополнительная информация о данном тарифе 3', reply_markup=inline_btn_request_tariff)
            await callback.answer()
        case "4 Offer":
            await callback.message.answer('Дополнительная информация о данном тарифе 4', reply_markup=inline_btn_request_tariff)
            await callback.answer()

@dp.callback_query_handler(text_startswith='send_')
async def send_offer(callback : types.CallbackQuery):
    try:
        match callback.data:
            case "send_request":
                print (callback.from_user.id)
                print (callback.from_user.first_name)
                print (callback.from_user.last_name)
                if (check_username(callback.from_user.id)[0][0] == 1):
                    await callback.message.answer('Your application is being processed, please wait for a response\n\nВаша заявка обрабатывается, дождитесь ответа')
                    await callback.answer()
                else:
                    await Form.name.set()
                    await callback.message.answer('Enter your name\n\nВведие ваше имя')
                    await callback.answer()
    except:
        await callback.message.answer('Something went wrong, error messages are processed by me as quickly as possible\n\nЧто-то пошло не так, сообщения об ошибках обрабатываются мной максимально быстро')
        await callback.answer()

@dp.callback_query_handler(text_startswith='Offer', state=Form)
async def send_offer(callback : types.CallbackQuery, state: FSMContext):
    match callback.data:
        case "1 Offer":
            await callback.message.answer('1')
            await callback.answer()
        case "2 Offer":
            await callback.message.answer('2')
            await callback.answer()
        case "3 Offer":
            await callback.message.answer('3')
            await callback.answer()
        case "4 Offer":
            await callback.message.answer('4')
            await callback.answer()

#  __________________________расписание_____________________________

async def get_schedule(message : types.Message):
    schedule = return_schedule()
    print(len(schedule))
    activities = ""
    for obj in schedule:
        print("_____________")
        ob = obj.return_activ()
        for activ in ob:
            print(activ)
            activities += activ + "\n"
        string = obj.day + "\n" + activities
        activities = ""
        await bot.send_message(message.from_user.id, string)

def register_handlers_client(dp: Dispatcher):
    FAQ=lambda c: c.data == 'FAQ'
    about=lambda c: c.data == 'about'
    offer=lambda c: c.data.find("Offer") > 0
    FAQ_Q=lambda c: c.data.find("_q") > 0
    dp.register_message_handler(command_start, commands=['start', 'старт'])
    dp.register_message_handler(get_schedule, commands=['расписание'])
    dp.register_message_handler(command_info, commands=['информация'])
    dp.register_message_handler(user_form_start, commands=['заявка'])
    dp.register_message_handler(cancel_handler, commands=['отмена_заявки'], state='*')
    dp.register_message_handler(tariffs_info, commands=['тарифы'])
    dp.register_message_handler(get_name, state=Form.name)
    dp.register_message_handler(get_phone, state=Form.phone)
    dp.register_message_handler(get_tariff_form, state=Form.tariff)
    dp.register_callback_query_handler(info_FAQ, FAQ)
    dp.register_callback_query_handler(info_about, about)
    dp.register_callback_query_handler(send_offer_prewiew, offer)
    dp.register_callback_query_handler(info_questions, FAQ_Q)