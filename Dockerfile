FROM lynnceptnetwork/lynnceptuserbot:slim-buster

#clonning repo 
RUN git clone https://github.com/LynnceptNetwork/LynnceptUserbot.git /root/LynnceptUserbot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install --no-cache-dir requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","lynnceptuserbot"]
