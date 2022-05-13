from aiogram import Dispatcher, types
from create_bot import dp, bot

# @dp.message_handler()
async def echo_send(message : types.Message):
    # await message.answer(message.text)
    # await message.reply(message.text)
    await bot.send_message(message.from_user.id, 'Сработал other.py')

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)