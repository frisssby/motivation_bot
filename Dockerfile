FROM ubuntu:20.04

RUN apt-get update && apt-get -y install python3-pip && \
pip3 install pyTelegramBotAPI

COPY bot.py .

ENTRYPOINT [ "python3", "bot.py" ]
