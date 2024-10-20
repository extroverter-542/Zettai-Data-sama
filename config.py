#(©)t.me/CodeFlix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7441037024:AAFvGtnkNBhG2RFWJ8zQfX1GdzwkLPkkxt0")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "19822764"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "b240e413364b8608a542a7cafc6903be")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001985214229"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "WhiteBeard_Sama")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1418213560"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://sanjisama626:sanjisama626@sanjisama.lukxw8r.mongodb.net/?retryWrites=true&w=majority&appName=sanjisama")
DB_NAME = os.environ.get("DATABASE_NAME", "Zettai_Data_sama_bot")
#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002075155178"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002037398576"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://envs.sh/wzR.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/wzz.jpg")

HELP_TXT = "<b>ᴛʜɪs ɪs ᴀɴ ᴀɴɪᴍᴇ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @Shirohige_Animes ...\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\nsɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ : <a href=https://t.me/Team_Onigashima>Mʏsᴛɪᴄ Nᴇxᴜs</a></b>"
ABOUT_TXT = "<b>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/WhiteBeard_Sama>Mʏsᴛɪᴄ Nᴇxᴜs</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/Team_Onigashima>𝐒ʜɪʀᴏʜɪɢᴇ</a>\n◈ ʜɪɴᴅɪ sᴜʙ ᴀɴɪᴍᴇ : <a href=https://t.me/Shirohige_Animes>𝐀ɴɪᴍᴇ 𝐃ʀɪғᴛ</a>\n◈ ʜɪɴᴅɪ ᴅᴜʙ ᴀɴɪᴍᴇ : <a href=https://t.me/Anime_Hindi_Dub_Officiall>𝐀ɴɪᴍᴇ 𝐙ᴇɴ</a>\n◈ ʜᴇᴍᴛᴀɪ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/+zPM3HDvFOvg5Yjg1>𝐂ʟɪᴄᴋ 𝐇ᴇʀᴇ</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/WhiteBeard_Sama>Mʏsᴛɪᴄ Nᴇxᴜs</a></b>"
START_MSG = os.environ.get("START_MESSAGE", "<b>Kᴏɴɴɪᴄʜɪᴡᴀ!! {mention}⚡,\n\nɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.\n\n𝐌ᴀɪɴ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Shirohige_Animes'>𝐀ɴɪᴍᴇ 𝐃ʀɪғᴛ</a></b>")
try:
    ADMINS=[1418213560]
    for x in (os.environ.get("ADMINS", "1418213560 5261438298 7344678908").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>𝐊ᴏɴɴɪᴄʜɪᴡᴀ!! {mention}✨,\n\n𝐏ʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴄʟɪᴄᴋ ᴏɴ • ᴛʀʏ ᴀɢᴀɪɴ • ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ᴀɴɪᴍᴇ ꜰɪʟᴇ.\n\n𝐌ᴀɪɴ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Shirohige_Animes'>𝐀ɴɪᴍᴇ 𝐃ʀɪғᴛ</a></b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!\n\nᴍʏ ᴏᴡɴᴇʀ : @Shirohige_Animes ..."

ADMINS.append(OWNER_ID)
ADMINS.append(1418213560)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
