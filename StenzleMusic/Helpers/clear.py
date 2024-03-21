
from StenzleMusic import Stenzledb
from StenzleMusic.Helpers import remove_active_chat


async def _clear_(chat_id):
    try:
        Stenzledb[chat_id] = []
        await remove_active_chat(chat_id)
    except:
        return
