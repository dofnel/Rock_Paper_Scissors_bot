import asyncio

from aiogram import Bot, Dispatcher
from handlers import rps_handlers
from config_data.config import Config, load_config


async def main():

    # Загружаем конфиг
    config = load_config('.env')

    dp: Dispatcher = Dispatcher()
    bot: Bot = Bot(config.tg_bot.token)

    # Регистрируем router из user_handlers в Dispatcher
    dp.include_router(rps_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
