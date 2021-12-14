#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @teamteleroid


from pyrogram import filters
from pyrogram import Client as trojanz
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import Config
from script import Script

from helpers.progress import PRGRS
from helpers.tools import clean_up
from helpers.download import download_file, DATA
from helpers.ffmpeg import extract_audio, extract_subtitle


@trojanz.on_callback_query()
async def cb_handler(client, query):

    if query.data == "start_data":
        await query.answer()
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("⭕ Channel ⭕", url="https://t.me/TeleRoidGroup"),
                InlineKeyboardButton("🛑 Support 🛑", url="https://t.me/TeleRoid14")],
            [InlineKeyboardButton("🆘 Help", callback_data="help_data"),
                InlineKeyboardButton("♂️ About", callback_data="about_data")],
            [InlineKeyboardButton("🔐 Close", callback_data="close")]
        ])

        await query.message.edit_text(
            Script.START_MSG.format(query.from_user.mention),
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return


    elif query.data == "help_data":
        await query.answer()
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🏡 Home", callback_data="start_data"),
                InlineKeyboardButton("♂️ About ", callback_data="about_data")],
            [InlineKeyboardButton("🛑 SUPPORT 🛑", url="https://t.me/TeleRoid14")]
        ])

        await query.message.edit_text(
            Script.HELP_MSG,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return


    elif query.data == "about_data":
        await query.answer()
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🆘 Help", callback_data="help_data"),
                InlineKeyboardButton("🏡 Home", callback_data="start_data")],
            [InlineKeyboardButton("SOURCE CODE", url="https://github.com/TeamTeleRoid/Streams-Extractor")]
        ])

        await query.message.edit_text(
            Script.ABOUT_MSG,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return


    elif query.data == "download_file":
        await query.answer()
        await query.message.delete()
        await download_file(client, query.message)


    elif query.data == "progress_msg":
        try:
            msg = "Progress Details...\n\n✅ Completed : {current}\n📃 Total Size : {total}\n🚀 Speed : {speed}\n⏳ Progress : {progress:.2f}%\n⏰ ETA: {eta}"
            await query.answer(
                msg.format(
                    **PRGRS[f"{query.message.chat.id}_{query.message.message_id}"]
                ),
                show_alert=True
            )
        except:
            await query.answer(
                "Processing your file...",
                show_alert=True
            )


    elif query.data == "close": 
        await query.message.delete()  
        await query.answer(
                "Cancelled...",
                show_alert=True
            ) 


    elif query.data.startswith('audio'):
        await query.answer()
        try:
            stream_type, mapping, keyword = query.data.split('_')
            data = DATA[keyword][int(mapping)]
            await extract_audio(client, query.message, data)
        except:
            await query.message.edit_text("** No Details Found**")   


    elif query.data.startswith('subtitle'):
        await query.answer()
        try:
            stream_type, mapping, keyword = query.data.split('_')
            data = DATA[keyword][int(mapping)]
            await extract_subtitle(client, query.message, data)
        except:
            await query.message.edit_text("**No Details Found**")  


    elif query.data.startswith('cancel'):
        try:
            query_type, mapping, keyword = query.data.split('_')
            data = DATA[keyword][int(mapping)] 
            await clean_up(data['location'])  
            await query.message.edit_text("**Cancelled...**")
            await query.answer(
                "Cancelled...",
                show_alert=True
            ) 
        except:
            await query.answer() 
            await query.message.edit_text("**No Details Found**")        
