
import asyncio
import importlib
import os

from pyrogram import idle

from StenzleMusic import (
    ASS_ID,
    ASS_NAME,
    ASS_USERNAME,
    BOT_ID,
    BOT_NAME,
    BOT_USERNAME,
    LOGGER,
    SUNAME,
    app,
    app2,
    pytgcalls,
)
from StenzleMusic.Modules import ALL_MODULES


async def stenzle_startup():
    try:
        LOGGER.info("[•] Loading Modules...")
        for module in ALL_MODULES:
            importlib.import_module("StenzleMusic.Modules." + module)
        LOGGER.info(f"[•] Loaded {len(ALL_MODULES)} Modules.")

        LOGGER.info("[•] Refreshing Directories...")
        if "downloads" not in os.listdir():
            os.mkdir("downloads")
        if "cache" not in os.listdir():
            os.mkdir("cache")
        LOGGER.info("[•] Directories Refreshed.")

        await app.send_message(
            SUNAME,
            f"✯ Stenzle ᴍᴜsɪᴄ ʙᴏᴛ ✯\n\n𖢵 ɪᴅ : `{BOT_ID}`\n𖢵 ɴᴀᴍᴇ : {BOT_NAME}\n𖢵 ᴜsᴇʀɴᴀᴍᴇ : @{BOT_USERNAME}",
        )

        await app2.send_message(
            SUNAME,
            f"✯ stenzle ᴍᴜsɪᴄ ᴀss ✯\n\n𖢵 ɪᴅ : `{ASS_ID}`\n𖢵 ɴᴀᴍᴇ : {ASS_NAME}\n𖢵 ᴜsᴇʀɴᴀᴍᴇ : @{ASS_USERNAME}",
        )

        await app2.send_message(BOT_USERNAME, "/start")

        LOGGER.info(f"[•] Bot Started As {BOT_NAME}.")
        LOGGER.info(f"[•] Assistant Started As {ASS_NAME}.")

        LOGGER.info("[•] Starting PyTgCalls...")
        await pytgcalls.start()
        LOGGER.info("[•] PyTgCalls Started Successfully.")

        await idle()

    except Exception as e:
        LOGGER.error(f"Error during startup: {str(e)}")
        raise


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(stenzle_startup())
    LOGGER.error("Stenzle Music Bot Stopped.")
