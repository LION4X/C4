# MIT License

# Copyright (c) 2021 subinps

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from config import Config
from instaloader import Profile
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong
import os
from utils import *
from time import sleep

USER = Config.USER
OWNER = Config.OWNER
HOME_TEXT_OWNER = Config.HOME_TEXT_OWNER
HELP = Config.HELP
HOME_TEXT = Config.HOME_TEXT
session = f"./{USER}"
STATUS = Config.STATUS
chat_idd = "1001383964791"

insta = Config.L
buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("👨🏼‍💻Developer", url='https://t.me/subinps'),
            InlineKeyboardButton("🤖Other Bots", url="https://t.me/subin_works/122")
        ],
        [
            InlineKeyboardButton("🔗Source Code", url="https://github.com/subinps/Instagram-Bot"),
            InlineKeyboardButton("🧩Deploy Own Bot",
                                 url="https://heroku.com/deploy?template=https://github.com/subinps/Instagram-Bot")
        ],
        [
            InlineKeyboardButton("👨🏼‍🦯How To Use?", callback_data="help#subin"),
            InlineKeyboardButton("⚙️Update Channel", url="https://t.me/subin_works")
        ]

    ]
)


@Client.on_message(filters.command("saved") & filters.private)
async def saved(bot, message):
    if str(message.from_user.id) != OWNER:
        await message.reply_text(
            HOME_TEXT.format(message.from_user.first_name, message.from_user.id, USER, USER, USER, OWNER),
            reply_markup=buttons,
            disable_web_page_preview=True
        )
        return
    text = message.text
    username = USER
    if 1 not in STATUS:
        await message.reply_text("You Must Login First /login ")
        return
    count = None
    if " " in text:
        cmd, count = text.split(' ')
    m = await message.reply_text(f"Fetching your Saved Posts.")
    chat_id = message.from_user.id
    dir = f"{chat_id}/{username}"
    x = 0
    for i in range(10):
        await m.edit("Starting Downloading..\nThis may take longer time Depending upon number of posts.")
        if count:
            command = [
                "instaloader",
                "--no-metadata-json",
                "--no-compress-json",
                "--no-profile-pic",
                "--no-posts",
                "--no-captions",
                "--no-video-thumbnails",
                "--login", USER,
                "-f", session,
                "--dirname-pattern", dir,
                ":saved",
                "--count", count
            ]
        else:
            command = [
                "instaloader",
                "--no-metadata-json",
                "--no-compress-json",
                "--no-profile-pic",
                "--no-posts",
                "--no-captions",
                "--no-video-thumbnails",
                "--login", USER,
                "-f", session,
                "--dirname-pattern", dir,
                ":saved"
            ]
        await download_insta(command, m, dir)
        await upload(m, bot, chat_id, chat_idd, dir)

        x += 1
        await bot.send_message(
            chat_id=chat_id,text="{}".format(x))

        sleep(1000)


