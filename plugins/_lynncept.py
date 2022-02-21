from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, eor, get_string, ultroid_cmd

REPOMSG = """
• **LYNNCEPT USERBOT** •\n
• Repo - [Click Here](https://github.com/LynnceptNetwork/LynnceptUserbot)
• Support - @Tanji_kamado_Support
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://github.com/LynnceptNetwork/LynnceptUserbot")
    ],
    [Button.url("Support Group", "t.me/tanji_kamado_support")],
]

ULTSTRING = """🎇 **Thanks for Deploying Lynncept Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@ultroid_cmd(
    pattern="repo$",
    type=["official", "manager"],
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info("Error while repo command : " + str(er))
    await eor(e, REPOMSG)


@ultroid_cmd(pattern="ultroid$")
async def useUltroid(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="https://telegra.ph/file/ebc333bd1cbf8c82e2721.jpg",
        buttons=button,
    )
    await eor(rs, f"**[Click Here]({msg.message_link})**")
