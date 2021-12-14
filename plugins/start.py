#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @teamteleroid


from pyrogram import filters
from pyrogram import Client as trojanz
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import Config
from script import Script


@trojanz.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    await message.reply_text(
        text=Script.START_MSG.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⭕ Channel ⭕", url="https://telegram.dog/TeleRoidGroup"),
                    InlineKeyboardButton("🛑 Support 🛑", url="https://telegram.dog/TeleRoid14"),
                ],
                [
                    InlineKeyboardButton("♂️ About", callback_data="about_data"),
                    InlineKeyboardButton("🆘 Help", callback_data="help_data"),
                ],
                [
                    InlineKeyboardButton(
                        "🔐 Close", callback_data="about_data")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
    )


@trojanz.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    await message.reply_text(
        text=Script.HELP_MSG,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🏡 Home ", callback_data="start_data"),
                    InlineKeyboardButton("♂️ About", callback_data="about_data"),
                ],
                [
                    InlineKeyboardButton(
                        "🤖 BotsList ", url="https://t.me/joinchat/t1ko_FOJxhFiOThl")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
    )


@trojanz.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    await message.reply_text(
        text=Script.ABOUT_MSG,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🆘 Help", callback_data="help_data"),
                    InlineKeyboardButton("🏡 Home", callback_data="start_data"),
                ],
                [
                    InlineKeyboardButton(
                        "SOURCE CODE", url="https://github.com/TeamTeleRoid/Streams-Extractor")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
    )
