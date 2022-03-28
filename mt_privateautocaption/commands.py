#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (C) PR0FESSOR-99

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

USERNAME = os.environ.get("BOT_USERNAME", "")

@Client.on_message(filters.private & filters.command("start"))
async def start(client, update):
    text = f"""✅ Hey I'm Alive"""
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
  )
