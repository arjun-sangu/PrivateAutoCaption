# Mo Tech YT

import os
import logging
import pyrogram

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("APP_ID", 12345))
API_HASH = os.environ.get("API_HASH", "")
    

if __name__ == "__main__" :
    plugins = dict(
        root="mt_privateautocaption"
    )
    CapBot = pyrogram.Client(
        "CaptionBot",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins,
        workers=300
    )
    CapBot.run()
