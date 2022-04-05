from subprocess import call
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from dataBase.execute_query import execute_query, paste_user
from create_bot import db_name, db_question
import aiogram.utils.markdown as md
from aiogram.types import ParseMode
import logging

from create_bot import dp, bot
from keyboards import btn_request_form, inline_btn_block_info, btn_block_tariffs, inline_btn_block_tariffs, inline_btn_block_q, inline_btn_request_tariff, btn_cancle_new_question
from schedule.schedule import return_schedule, Schedule_ob

class Form(StatesGroup):
    name = State()
    tariff = State()
    phone = State()
    nickname = State()
    tg_id = State()
    status = State()

class SendQuestion(StatesGroup):
    text_q = State()

#  __________________________старт_____________________________

async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Hello, I was created to introduce you to telegram-bots. If you see this message, you have started a dialogue with me, and here can be any message that you want to show to anyone who starts a dialogue with me\n\nЗдравствуйте, я создан, чтобы познакомить вас с телеграм-ботами. Если вы видите это сообщение, вы начали диалог со мной, и здесь может быть любое сообщение, которое вы хотите показать всем, кто начинает диалог со мной.\nДля получения доступа к управлению заявками намипишите мне: https://t.me/kritinidzin', reply_markup=btn_request_form)
    except:
        await message.answer('Something went wrong, error messages are processed by me as quickly as possible\n\nЧто-то пошло не так, сообщения об ошибках обрабатываются мной максимально быстро')

def check_username(userid, db_name, query):
    id = execute_query(db_name, query)
    return id

#  __________________________форма_____________________________

async def user_form_start(message : types.Message):
    try:
        query = "SELECT EXISTS(SELECT tg_id FROM bot WHERE tg_id = '" + str(message.from_user.id) + "' AND status = 1)"
        if (check_username(message.from_user.id, db_name, query)[0][0] == 1):
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
    stmt = "INSERT INTO `bot`(`name`, `phone`, `tg_id`, `nickname`, `status`, `tariff`) VALUES (?, ?, ?, ?, ?, ?)"
    paste_user(db_name, stmt, user)
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
            await callback.message.answer("Ответ на 1 вопрос")
            await callback.answer()
        case "2_q":
            await callback.message.answer("Ответ на 2 вопрос")
            await callback.answer()
        case "3_q":
            await callback.message.answer("Ответ на 3 вопрос")
            await callback.answer()
        case "4_q":
            await callback.message.answer("Ответ на 4 вопрос")
            await callback.answer()
        case "5_q":
            await callback.message.answer("Ответ на 5 вопрос")
            await callback.answer()
        case "new_q":
            query = "SELECT EXISTS(SELECT id_tg FROM question WHERE id_tg = '" + str(callback.from_user.id) + "' AND status = 1)"
            if (check_username(callback.from_user.id, db_question, query)[0][0] == 1):
                await callback.message.answer('Ваш вопрос передан, мы его обработаем и отправим ответ лично вам, если подобный вопрос задаст большое количество людей, то вы его сможете найти в списке выше')
                await callback.answer()
            else:
                await callback.message.answer("Введите ваш вопрос", reply_markup=btn_cancle_new_question)
                await SendQuestion.text_q.set()
                await callback.answer()

async def cancel_form_question(message: types.Message, state: SendQuestion):
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.answer('Отправка вопроса была успешно прекращена', reply_markup=btn_request_form)
    await state.finish()
    
async def get_text_question(message: types.Message, state: SendQuestion):
    async with state.proxy() as data:
        data['text_q'] = message.text
    user = [
        (data['text_q'],
        message.from_user.id,
        message.from_user.username,
        1)
    ]
    print(user)
    await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Вопрос: ', user[0][0]),
                md.text('ID: ', user[0][1]),
                md.text('Nickname: ', user[0][2]),
                md.text('Статус: ', user[0][3]),
                sep='\n',
            ),
            parse_mode=ParseMode.MARKDOWN,
        )
    stmt = "INSERT INTO `question`(`question`, `id_tg`, `nickname`, `status`) VALUES (?, ?, ?, ?)"
    paste_user(db_name=db_question, stmt=stmt, user=user)
    await state.finish()
    await message.answer("Ваш вопрос передан, мы его обработаем и отправим ответ лично вам, если подобный вопрос задаст большое количество людей, то вы его сможете найти в списке выше", reply_markup=btn_request_form)

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
    dp.register_message_handler(cancel_form_question, commands=['отмена_вопроса'], state='*')
    dp.register_message_handler(get_text_question, state=SendQuestion.text_q)
    dp.register_callback_query_handler(info_FAQ, FAQ)
    dp.register_callback_query_handler(info_about, about)
    dp.register_callback_query_handler(send_offer_prewiew, offer)
    dp.register_callback_query_handler(info_questions, FAQ_Q)