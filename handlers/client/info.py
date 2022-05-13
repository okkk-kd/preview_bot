from create_bot import bot, dp, db_question

from src.check_user import check_username

from dataBase.execute_query import paste_user

from aiogram.types import ParseMode
import aiogram.utils.markdown as md

from keyboards.request import inline_btn_block_info, \
    btn_uni_select_kb, \
    btn_cancel_new_question, \
    btn_request_form

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


class SendQuestion(StatesGroup):
    text_q = State()

async def command_info(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Здесь может располагаться любая ваша информация, пример вы можете видеть сами:', reply_markup=inline_btn_block_info)
    except:
        await message.answer('Что-то пошло не так, сообщения об ошибках обрабатываются мной максимально быстро')

async def info_FAQ(callback : types.CallbackQuery):
    await callback.message.answer("Here you can find answers to frequently asked questions\n\nЗдесь вы модете найти ответ на часто задаваемые вопросы", reply_markup=btn_uni_select_kb)
    # inline_btn_block_q
    await callback.answer()

async def info_about(callback : types.CallbackQuery):
    await callback.message.answer(callback.data)
    await callback.answer()

async def info_questions(callback : types.CallbackQuery):
    if (callback.data == "1_q"):
        await callback.message.answer("Ответ на 1 вопрос")
        await callback.answer()
    elif (callback.data == "2_q"):
        await callback.message.answer("Ответ на 2 вопрос")
        await callback.answer()
    elif (callback.data == "3_q"):
        await callback.message.answer("Ответ на 3 вопрос")
        await callback.answer()
    elif (callback.data == "4_q"):
        await callback.message.answer("Ответ на 4 вопрос")
        await callback.answer()
    elif (callback.data == "5_q"):
        await callback.message.answer("Ответ на 5 вопрос")
        await callback.answer()
    elif (callback.data == "new_q"):
        query = "SELECT EXISTS(SELECT id_tg FROM question WHERE id_tg = '" + str(callback.from_user.id) + "' AND status = 1)"
        if (check_username(callback.from_user.id, db_question, query)[0][0] == 1):
            await callback.message.answer('Ваш вопрос передан, мы его обработаем и отправим ответ лично вам, если подобный вопрос задаст большое количество людей, то вы его сможете найти в списке выше')
            await callback.answer()
        else:
            await callback.message.answer("Введите ваш вопрос", reply_markup=btn_cancel_new_question)
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


def register_handlers_info(dp: Dispatcher):
    FAQ=lambda c: c.data == 'FAQ'
    FAQ_Q=lambda c: c.data.find("_q") > 0
    about=lambda c: c.data == 'about'
    dp.register_message_handler(cancel_form_question, commands=['отмена_вопроса'], state='*')
    dp.register_message_handler(get_text_question, state=SendQuestion.text_q)
    dp.register_callback_query_handler(info_FAQ, FAQ)
    dp.register_callback_query_handler(info_about, about)
    dp.register_callback_query_handler(info_questions, FAQ_Q)
    dp.register_message_handler(command_info, commands=['информация'])