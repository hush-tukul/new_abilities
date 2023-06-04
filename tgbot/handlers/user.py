import logging
import time

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, BufferedInputFile

from tgbot.handlers.insta_loader import download_instagram_video

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.reply("Вітаю, користувач!")




# @user_router.message(F.text)
# async def instalink(message: Message):
#     g = ['www.instagram.com/p', 'www.instagram.com/reel']
#     if any([True if i in message.text else False for i in g]):
#         logging.info("trying to download video")
#
#         start = time.time()
#         link = message.text
#
#         r = await download_instagram_video(link, message.from_user.id)
#         end = time.time()
#         input_file_d = BufferedInputFile(r, filename="cut_video.mp4")
#         await message.answer_video(input_file_d,
#                                    caption=f"File converted successfully!\nTime: {round(end - start, 3)} seconds")
