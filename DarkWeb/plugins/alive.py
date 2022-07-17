# Thanks to @D3_krish
# Porting in DARKDarkWeb
import asyncio
from telethon import version

from DarkWeb import ALIVE_NAME, darkversion
from DarkWeb.cmdhelp import CmdHelp
from DarkWeb.Config.DARK_Config import Config
from DarkWeb.utils import admin_cmd, sudo_cmd
from DarkWeb import *

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARK WEB"

ludosudo = Config.SUDO_USERS

sudou = "True" if ludosudo else "False"
DARK = bot.uid

edit_time = 1
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/b765c0daec4a63c286e34.mp4"
""" =======================CONSTANTS====================== """
pm_caption = "  __**🔥🔥𝐑𝐄𝐁𝐄𝐋 𝐁𝐎𝐓  𝐈𝐒 𝐀𝐋𝐈𝐕𝐄🔥🔥**__\n\n" + "**━━━━━━━━━━━━━━━━━━━━━━**\n\n"


pm_caption += (
    f"                🔰ᗰᗩՏTᗴᖇ🔰\n      **『[{DEFAULTUSER}](tg://user?id={DARK})』**\n\n"
)
pm_caption += "┏━━━━━━━━━━━━━\n"
pm_caption += f"┣•➳➠  `ᴛᴇʟᴇᴛʜᴏɴ:` `{version.__version__}` \n"
pm_caption += f"┣•➳➠ `ᴠᴇʀsɪᴏɴ:` `{DARKversion}`\n"
pm_caption += f"┣•➳➠ `sᴜᴅᴏ:` `{sudou}`\n"
pm_caption += "┣•➳➠ `ᴄʜᴀɴɴᴇʟ:` [ᴊᴏɪɴ](https://t.me/DarkWeb_SUPPORT)\n"
pm_caption += "┣•➳➠ `ᴄʀᴇᴀᴛᴏʀ:` [ʀᴇʙᴇʟ](https://t.me/DARK_IS_OP)\n"
pm_caption += "┣•➳➠ `sᴜᴘᴘᴏʀᴛᴇʀ:` [sᴜᴘᴘᴏʀᴛ](https://t.me/DARKSSUPPORT)\n"
pm_caption += "┗━━━━━━━━━━━━━━━\n"
pm_caption += " [🔥𝚁𝙴𝙿𝙾🔥](https://github.com/TEAMDARKS/DarkWeb) 🔹 [📜𝙻𝚒𝚌𝚎𝚗𝚜𝚎📜](https://github.com/TEAMDARKS/DarkWeb/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1, caption=pm_caption)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()


CmdHelp("alive").add_command("alive", None, "To check am i alive").add_command(
    "DARK", None, "To check am i alive with your favorite alive pic"
).add()
