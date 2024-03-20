

from pyrogram import filters
from pyrogram.types import Message

from StenzleMusic import app, pytgcalls
from StenzleMusic.Helpers import admin_check, close_key, is_streaming, stream_on


@app.on_message(filters.command(["resume"]) & filters.group)
@admin_check
async def res_str(_, message: Message):
    try:
        await message.delete()
    except:
        pass

    if await is_streaming(message.chat.id):
    await stream_on(message.chat.id)
    await pytgcalls.resume_stream(message.chat.id)
    
