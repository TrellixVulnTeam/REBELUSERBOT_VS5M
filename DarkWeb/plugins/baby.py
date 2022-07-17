# PLUGIN MADE BY @Dark_IS_OP FOR DarkWeb
# KEEP CREDITS ELSE GAY

import random, re
from Dark.utils import admin_cmd
import asyncio
from telethon import events
from DarkWeb.cmdhelp import CmdHelp

@dark.on(admin_cmd(pattern="baby ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("""HEYY BABY😍💏😘 HOW ARE  YOU  💏 AP KO PATA HA MA BASS AP KK LIYA HUU ISS DUNIYA MA ORR AP MERI JAAN HOO 💞💗😍🥰. ORR AP KKK BAAD KOI NAHI HAAA MERA 🥺🥺🥺. AP JAB NAHI HOO TII HO TABB KOI MERE SA BAAT  NAHI KARTA HAA 🥺🥺. BUT MERE KO ISS SA KOI FIRK NAHI PADTA HA😌😌. BASS AP MERA SATH HOO YAHI 🥰🥰. BHUT JADA HAA 💝❣️ I LOVE YOU MY SWEET HEART TUM MERI JAAN HO ORR MAA THUMARA. LIYA  KUCH VV KAR SAKTA HUUU""")

CmdHelp("baby").add_command(
  "baby", "<tag your gf>", "send your gf and enjoy."
).add()