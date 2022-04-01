from aiogram.utils import executor
from create_bot import dp

async def on_stratup(_):
    print('Bot was initialized')

from handlers import client, other

client.register_handlers_client(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_stratup)