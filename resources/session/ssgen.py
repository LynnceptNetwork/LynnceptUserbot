#!/usr/bin/python3
# Lynncept - UserBot
# Copyright (C) 2021 LynnceptNetwork
#
# This file is a part of < https://github.com/LynnceptNetwork/LynnceptUserbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/LynnceptNetwork/LynnceptUserbot/blob/main/LICENSE/>.

import os
from time import sleep

a = r"""
LynnceptNetwork Providing you The LynnceptUserbot!!
"""


def spinner():
    print("Checking if Telethon is installed...")
    for _ in range(3):
        for frame in r"-\|/-\|/":
            print("\b", frame, sep="", end="", flush=True)
            sleep(0.1)
    import telethon


def clear_screen():
    # https://www.tutorialspoint.com/how-to-clear-screen-in-python#:~:text=In%20Python%20sometimes%20we%20have,screen%20by%20pressing%20Control%20%2B%20l%20.
    if os.name == "posix":
        os.system("clear")
    else:
        # for windows platfrom
        os.system("cls")


def get_api_id_and_hash():
    print(
        "Get your API ID and API HASH from my.telegram.org to proceed.\n\n",
    )
    try:
        API_ID = int(input("Please enter your API ID: "))
    except ValueError:
        print("APP ID must be an integer.\nQuitting...")
        exit(0)
    API_HASH = input("Please enter your API HASH: ")
    return API_ID, API_HASH


def telethon_session():
    try:
        spinner()

        x = "\bFound an existing installation of Telethon...\nSuccessfully Imported.\n\n"
    except ImportError:
        print("Installing Telethon...")
        os.system("pip install -U telethon")

        x = "\bDone. Installed and imported Telethon."
    clear_screen()
    print(a)
    print(x)

    # the imports

    from telethon.errors.rpcerrorlist import ApiIdInvalidError, PhoneNumberInvalidError
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient

    API_ID, API_HASH = get_api_id_and_hash()

    # logging in
    try:
        with TelegramClient(StringSession(), API_ID, API_HASH) as ultroid:
            print("Generating a user session for LynnceptUserbot...")
            ult = ultroid.send_message(
                "me",
                f"**LYNNCEPTUSERBOT** `SESSION`:\n\n`{LynnceptUserbot.session.save()}`\n\n**Do not share this anywhere!**",
            )
            print(
                "Your SESSION has been generated. Check your telegram saved messages!"
            )
    except ApiIdInvalidError:
        print(
            "Your API ID/API HASH combination is invalid. Kindly recheck.\nQuitting..."
        )
    except ValueError:
        print("API HASH must not be empty!\nQuitting...")
    except PhoneNumberInvalidError:
        print("The phone number is invalid!\nQuitting...")
    except Exception as er:
        print(er)

def main():
    clear_screen()
    print(a)
    telethon_session()
    x = input("Run again? (y/n)")
    if x.lower() == "y":
        main()
    else:
        exit(0)


main()
