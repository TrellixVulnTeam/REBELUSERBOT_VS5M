import asyncio

from REBELBOT.Config import Config
from REBELBOT.utils import admin_cmd, sudo_cmd
from userbot.smex.DARK_Config import Config
from userbot.cmdhelp import CmdHelp
from userbot import REBELBOT_ID, SUDO_USERS

LOGGER = Config.REBELBOT_ID
SUDO_WALA = Config.SUDO_USERS


@bot.on(admin_cmd(pattern="spam (.*)"))
@bot.on(sudo_cmd(pattern="spam (.*)", allow_sudo=True))
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])
        await asyncio.wait([e.respond(spam_message) for _ in range(counter)])
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER, "#SPAM \n\n" "Spam was executed successfully"
            )


@bot.on(admin_cmd(pattern="bigspam"))
@bot.on(sudo_cmd(pattern="bigspam", allow_sudo=True))
async def bigspam(REBEL):
    if not REBEL.text[0].isalpha() and REBEL.text[0] not in ("/", "#", "@", "!"):
        REBEL_msg = REBEL.text
        REBELBOT_count = int(REBEL_msg[9:13])
        REBEL_spam = str(REBEL.text[13:])
        for _ in range(1, REBELBOT_count):
            await REBEL.respond(REBEL_spam)
        await REBEL.delete()
        if LOGGER:
            await REBEL.client.send_message(
                LOGGER, "#BIGSPAM \n\n" "Bigspam was executed successfully"
            )


@bot.on(admin_cmd("dspam (.*)"))
@bot.on(sudo_cmd(pattern="dspam (.*)", allow_sudo=True))
async def spammer(e):
    if e.fwd_from:
        return
    input_str = "".join(e.text.split(maxsplit=1)[1:])
    spamDelay = float(input_str.split(" ", 2)[0])
    counter = int(input_str.split(" ", 2)[1])
    spam_message = str(input_str.split(" ", 2)[2])
    await e.delete()
    for _ in range(counter):
        await e.respond(spam_message)
        await asyncio.sleep(spamDelay)


# @register(outgoing=True, pattern="^.mspam (.*)")
@bot.on(admin_cmd(pattern="mspam (.*)"))
@bot.on(sudo_cmd(pattern="mspam (.*)", allow_sudo=True))
async def tiny_pic_spam(e):
    sender = await e.get_sender()
    me = await e.client.get_me()
    if sender.id != me.id and not SUDO_WALA:
        return await e.reply("`Sorry sudo users cant access this command..`")
    try:
        await e.delete()
    except:
        pass
    try:
        counter = int(e.pattern_match.group(1).split(" ", 1)[0])
        reply_message = await e.get_reply_message()
        if not reply_message or not e.reply_to_msg_id or not reply_message.media:
            return await e.edit("```Reply to a pic/sticker/gif/video message```")
        message = reply_message.media
        for _ in range(1, counter):
            await e.client.send_file(e.chat_id, message)
    except:
        return await e.reply(
            "**Error**\nUsage `!mspam <count> reply to a sticker/gif/photo/video`"
        )


CmdHelp("spam").add_command(
    "spam", "<number> <text>", "Sends the text 'X' number of times.", ".spam 99 Hello"
).add_command(
    "mspam",
    "<reply to media> <number>",
    "Sends the replied media (gif/ video/ sticker/ pic) 'X' number of times",
    ".mspam 100 <reply to media>",
).add_command(
    "dspam",
    "<delay> <spam count> <text>",
    "Sends the text 'X' number of times in 'Y' seconds of delay",
    ".dspam 5 100 Hello",
).add_command(
    "bigspam",
    "<count> <text>",
    "Sends the text 'X' number of times. This what REBELBOT iz known for. The Best BigSpam Ever",
    ".bigspam 5000 Hello",
).add()
