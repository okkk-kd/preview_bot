FROM ubuntu:latest

RUN mkdir /usr/src/helpUniBot
RUN sudo apt update && sudo apt install python3.9 -y
WORKDIR /usr/src/helpUniBot

COPY . /usr/src/helpUniBot
RUN python3 -m venv venv && pip install -r requirements.txt
CMD ["python3", "main.py"]