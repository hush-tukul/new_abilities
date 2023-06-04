import logging
import time

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, BufferedInputFile
from aiogram_dialog import DialogManager

from run import dp, bot
from tgbot.handlers.insta_loader import download_instagram_video, InstaLogin
from tgbot.filters.admin import AdminFilter

admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.message(CommandStart())
async def admin_start(message: Message):
    await message.reply("Вітаю, адміне!")





# @admin_router.message(F.text)
# async def instalink(message: Message):
#     g = ['www.instagram.com/p', 'www.instagram.com/reel']
#     if any([True if i in message.text else False for i in g]):
#         logging.info("trying to download video")
#
#         cl = await dp.storage.get_data(bot=bot, key='cl')
#         start = time.time()
#         link = message.text
#         logging.info(cl)
#         r = await download_instagram_video(link, message.from_user.id, cl['cl'])
#         end = time.time()
#         input_file_d = BufferedInputFile(r, filename="cut_video.mp4")
#         await message.answer_video(input_file_d,
#                                    caption=f"File converted successfully!\nTime: {round(end - start, 3)} seconds")
