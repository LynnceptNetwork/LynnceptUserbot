# Lynncept - UserBot
# Copyright (C) 2021 LynnceptNetwork
# This file is a part of < https://github.com/LynnceptNetwork/LynnceptUserbot/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/LynnceptNetwork/LynnceptUserbot/blob/main/LICENSE/>.

FROM lynnceptnetwork/lynnceptuserbot:main

# set timezone
ENV TZ=Asia/Kolkata

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \

    # cloning the repo and installing requirements.
    && git clone https://github.com/LynnceptNetwork/LynnceptUserbot.git /root/LynnceptNetwork/ \
    && pip3 install --no-cache-dir -r root/LynnceptNetwork/requirements.txt \
    && pip3 uninstall av -y && pip3 install av --no-binary av

# changing workdir
WORKDIR /root/LynnceptNetwork/

# start the bot
CMD ["bash", "resources/startup/startup.sh"]
