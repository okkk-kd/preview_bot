from aiogram.utils import executor
from create_bot import dp

async def on_stratup(_):
    print('Bot was initialized')

from handlers import other, admin
from handlers.client.request_form import register_handlers_request_form
from handlers.client.start import register_handlers_start
from handlers.client.info import register_handlers_info

register_handlers_start(dp)
register_handlers_request_form(dp)
register_handlers_info(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_stratup)