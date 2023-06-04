import asyncio
import logging

import betterlogging as bl
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from aiogram.types import BotCommand

from run import bot, dp
from tgbot.config import load_config
from tgbot.handlers.admin import admin_router
from tgbot.handlers.echo import echo_router
from tgbot.handlers.insta_loader import InstaLogin
from tgbot.handlers.user import user_router
from tgbot.middlewares.config import ConfigMiddleware
from tgbot.services import broadcaster

logger = logging.getLogger(__name__)
log_level = logging.INFO
bl.basic_colorized_config(level=log_level)


async def on_startup(bot: Bot, admin_ids: list[int]):
    await broadcaster.broadcast(bot, admin_ids, "Бот був запущений")


def register_global_middlewares(dp: Dispatcher, config):
    dp.message.outer_middleware(ConfigMiddleware(config))
    dp.callback_query.outer_middleware(ConfigMiddleware(config))


async def set_default_commands(dp):
    commands = [
        BotCommand(command="start", description="Запустити бота/Start the bot/Запустить бота"),
        BotCommand(command="info", description="Опис можливостей бота/Description of bot functions/Описание возможностей бота"),
    ]
    await bot.set_my_commands(commands)
    await bot.set_chat_menu_button()



async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")


    for router in [
        admin_router,
        user_router,
        echo_router
    ]:
        dp.include_router(router)
    insta_login = InstaLogin()
    insta_login.login()
    cl = insta_login.cl
    data = [{'cl', cl}]
    await dp.storage.update_data(bot=bot, key='cl', data=data)
    register_global_middlewares(dp, config)
    await bot.delete_webhook(drop_pending_updates=True)
    await on_startup(bot, config.tg_bot.admin_ids)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Бот був вимкнений!")
