# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'ok'


# import telebot

# bot = telebot.TeleBot('366514649:AAEL4gxETw62Rw1fdDoHuVB8MlVQpUeNtJY')
#
#
# @bot.message_handler(func=lambda message: True, content_types=['text'])
# def echo_message(message):
#     bot.reply_to(message.chat.id, message.text)
#


if __name__ == '__main__':
    app.run()
    # bot.polling(none_stop=True)
