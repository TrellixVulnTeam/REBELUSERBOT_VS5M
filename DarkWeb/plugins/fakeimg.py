import requests
from DarkWeb import CmdHelp
from Dark.utils import edit_or_reply, admin_cmd, sudo_cmd
import os


@Dark.on(admin_cmd(pattern="picgen"))
@Dark.on(sudo_cmd(pattern="picgen", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    
    url = "https://thispersondoesnotexist.com/image"
    response = requests.get(url)
    await event.edit("`Creating a fake face...`")
    if response.status_code == 200:
      with open("DarkWeb.jpg", 'wb') as f:
        f.write(response.content)
    
    captin = f"Fake Image By DarkWeb."
    fole = "DarkWeb.jpg"
    await borg.send_file(event.chat_id, fole, caption=captin)
    await event.delete()
    os.system("rm /root/userbot/DarkWeb.jpg ")