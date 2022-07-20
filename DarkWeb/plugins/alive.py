import asyncio
import time
from telethon import version

from DarkWeb import ALIVE_NAME, darkversion, StartTime
from DarkWeb.cmdhelp import CmdHelp
from DarkWeb.smex.DARK_Config import Config
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
pm_caption += f"┣•➳➠ `ᴠᴇʀsɪᴏɴ:` `{darkversion}`\n"
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
    DarkWeb = await edit_or_reply(alive, "`Building Alive....`")
    await alive.get_chat()
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1, caption=pm_caption)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()


async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "DARK WEB"
DARK_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "LEGENDARY AF DARK WEB"
mention = f"[{DEFAULTUSER}](tg://user?id={bot.uid})"

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += f"{time_list.pop()}, "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


REBEL_caption = """
                  {CUSTOM_ALIVE_TEXT}**\n\n
                   ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n
                    __**ʙᴏᴛ sᴛᴀᴛᴜs**__\n\n
                    ➪ ᴛᴇʟᴇᴛʜᴏɴ : `1.24.0`\n
                    ➪ ʀᴇʙᴇʟʙᴏᴛ : `3.2`\n
                    ➪ ᴜᴘᴛɪᴍᴇ   : `{uptime}\n`
                    ➪ ᴍᴀsᴛᴇʀ    :** {mention}\n
"""

@dark.on(admin_cmd(outgoing=True, pattern="rebel$"))
@dark.on(sudo_cmd(pattern="rebel$", allow_sudo=True))
async def amireallyalive(alive):
    DarkWeb = await edit_or_reply(alive, "`ɖaʀӄաɛɮ ɮօȶ ɨֆ օռʟɨռɛ`")
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
   
        await alive.client.send_file(
            alive.chat_id, DARK_IMG, caption=REBEL_caption, reply_to=reply_to_id
            )
        await alive.delete()

CmdHelp("alive").add_command("alive", None, "To check am i alive").add_command(
    "dark", None, "To check am i alive with your favorite alive pic"
).add()
