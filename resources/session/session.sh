#!/usr/bin/env bash
# Lynncept - UserBot
# Copyright (C) 2021 LynnceptNetwork
#
# This file is a part of < https://github.com/LynnceptNetwork/LynnceptUserbot/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/LynnceptNetwork/LynnceptUserbot/blob/main/LICENSE/>.

clear
echo -e "\e[1m"
echo "__________________________________________"
echo " |                                      |"
echo " |                                      |"
echo " | LynnceptUserbot by @LynnceptNetwork  |"
echo " |                                      |"
echo " |______________________________________|"
echo -e "\e[0m"
sec=5
spinner=(⣻ ⢿ ⡿ ⣟ ⣯ ⣷)
while [ $sec -gt 0 ]; do
    echo -ne "\e[33m ${spinner[sec]} Starting dependency installation in $sec seconds...\r"
    sleep 1
    sec=$(($sec - 1))
done
echo -e "\e[1;32mInstalling Dependencies ---------------------------\e[0m\n" # Don't Remove Dashes / Fix it
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/LynnceptNetwork/LynnceptUserbot/main/resources/session/ssgen.py
pip install telethon
clear
python3 ssgen.py
