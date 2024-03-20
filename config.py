from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG" , "https://graph.org/file/26fb6a3ccf7f40e28bd61.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/41eba98d63d89f1f5b6a2.png")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Mallus_Street")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Techno_Bullets")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7089056796 7044382449").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
