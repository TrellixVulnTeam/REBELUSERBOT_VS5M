import asyncio
import os
import random
import re
import urllib

import requests
from REBELBOT.utils import admin_cmd
from telethon.tl import functions

COLLECTION_STRINGZ = [
    "shiv-photo-wallpapers",
]


async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRINGZ) - 1)

    pack = COLLECTION_STRINGZ[rnd]

    pc = requests.get(f"http://getwallpapers.com/collection/{pack}").text

    f = re.compile("/\w+/full.+.jpg")

    f = f.findall(pc)

    fy = f"http://getwallpapers.com{random.choice(f)}"

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )

    urllib.request.urlretrieve(fy, "donottouch.jpg")


@borg.on(admin_cmd(pattern="adshiv ?(.*)"))
async def main(event):

    await event.edit(
        "**Starting shiv Profile Pic...\n\nDone !!! Check Your DP. Made by @veryhelpful"
    )

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")

        await event.client(functions.photos.UploadProfilePhotoRequest(file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(300)
