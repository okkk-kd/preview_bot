from src.check_user import check_username
from src.get_arr import get_arr
from src.is_str_same import is_str_same

from handlers.client.callback.uni_sellection_call import register_callback_handlers_uni_selection
from handlers.client.callback.direction_sellection_call import register_callback_handlers_dir_selection
from handlers.client.callback.course_selection_call import register_callback_handlers_course_selection
from handlers.client.callback.work_sellection_call import register_callback_handlers_work_selection

from keyboards.request import btn_uni_select_kb, \
    btn_request_form, \
    btn_dir_select_kb, \
    btn_cours_sellection_kb, \
    btn_work_sellection_kb

from create_bot import db_name, bot, dp

from dataBase.execute_query import paste_user

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
import aiogram.utils.markdown as md

from aiogram.dispatcher import FSMContext
from src.parse_digit import parse_digit

class Form(StatesGroup):
    uni = State()
    direction = State()
    course = State()
    type_work = State()
    theme = State()
    file = State()
    nickname = State()
    tg_id = State()
    status = State()

async def user_form_start(message : types.Message):
    try:
        query = "SELECT EXISTS(SELECT tg_id FROM bot WHERE tg_id = '" + str(message.from_user.id) + "' AND status = 1)"
        if (check_username(message.from_user.id, db_name, query)[0][0] == 1):
            await message.answer('Ваша заявка обрабатывается, дождитесь ответа')
        else:
            await Form.uni.set()
            await message.answer('Выберите из списка университет', reply_markup=btn_uni_select_kb)
    except:
        await message.answer('Что-то пошло не так, сообщения об ошибках обрабатываются мной максимально быстро')

async def cancel_handler(message: types.Message, state: Form):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('Отмена произошла успешно')

register_callback_handlers_uni_selection(dp, state=Form)

async def uni_button_select(query: types.CallbackQuery, state: FSMContext):
    if (len(get_arr("uni.txt")) > parse_digit(query.data)):
        await state.update_data(uni=get_arr("uni.txt")[parse_digit(query.data)])
        await state.set_state(Form.direction)
        await query.message.answer('Выберите из списка направление', reply_markup=btn_dir_select_kb)

register_callback_handlers_dir_selection(dp, state=Form)

async def dir_button_select(query: types.CallbackQuery, state: FSMContext):
    if (len(get_arr("direction.txt")) > parse_digit(query.data)):
        await state.update_data(direction=get_arr("direction.txt")[parse_digit(query.data)])
        await state.set_state(Form.course)
        await query.message.answer('Выберите из списка курс', reply_markup=btn_cours_sellection_kb)

register_callback_handlers_course_selection(dp, state=Form)

async def course_button_select(query: types.CallbackQuery, state: FSMContext):
    if (len(get_arr("course.txt")) > parse_digit(query.data)):
        await state.update_data(course=get_arr("course.txt")[parse_digit(query.data)])
        await state.set_state(Form.type_work)
        await query.message.answer('Выберите из списка тип работы', reply_markup=btn_work_sellection_kb)

register_callback_handlers_work_selection(dp, state=Form)

async def work_button_select(query: types.CallbackQuery, state: FSMContext):
    if (len(get_arr("type_of_work.txt")) > parse_digit(query.data)):
        await state.update_data(type_work=get_arr("type_of_work.txt")[parse_digit(query.data)])
        await state.set_state(Form.theme)
        await query.message.answer('Введите тему работы')


async def get_theme(message: types.Message, state: Form):
    async with state.proxy() as data:
        data['theme'] = message.text
        data['tg_id'] = message.from_user.id
        data['nickname'] = message.from_user.username
        data['status'] = 1
    await Form.next()
    await message.answer('Отправте файл с заданием', reply_markup=btn_request_form)


async def get_file(message: types.Message, state: Form):
    async with state.proxy() as data:
        data['file'] = message.text
    user = [
        (data['uni'],
        data['direction'],
        data['course'],
        data['type_work'],
        data['theme'],
        data['tg_id'],
        data['nickname'],
        data['status'])
    ]
    condition = lambda a : "Обрабатывается" if (a == 1) else "Ошибка обработки, уже решаем вашу проблему"
    await bot.send_message(
            
            message.chat.id,
            md.text(
                md.text('Университет: ', data['uni']),
                md.text('Направление: ', data['direction']),
                md.text('Курс: ', data['course']),
                md.text('Имя пользователя: ', data['nickname']),
                md.text('Статус: ', condition(data['status'])),
                sep='\n',
            ),
            parse_mode=ParseMode.MARKDOWN,
        )
    stmt = "INSERT INTO `bot`(`uni`, `direction`, `course`, `type_work` , `theme` ,`tg_id`, `nickname`, `status`) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    paste_user(db_name, stmt, user)
    await state.finish()

def register_handlers_request_form(dp: Dispatcher):
    uni_pages=lambda c: c.data.startswith("uni_")
    dir_pages=lambda c: c.data.startswith("dir_")
    course_pages=lambda c: c.data.startswith("course_")
    work_pages=lambda c: c.data.startswith("work_")
    dp.register_callback_query_handler(work_button_select, work_pages, state=Form)
    dp.register_callback_query_handler(dir_button_select, dir_pages, state=Form)
    dp.register_callback_query_handler(uni_button_select, uni_pages, state=Form)
    dp.register_callback_query_handler(course_button_select, course_pages, state=Form)
    dp.register_message_handler(cancel_handler, commands=['отмена'], state='*')
    dp.register_message_handler(get_theme, state=Form.theme)
    dp.register_message_handler(get_file, state=Form.file)
    dp.register_message_handler(user_form_start, commands=['заявка'])
    