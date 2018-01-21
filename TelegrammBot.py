
import telebot
import math
import re
import datetime
import time
import json
from pprint import pprint
from db01 import add_user
token = '450087644:AAHREmBtANmyRbDu4uxVc3I7tK--L0qcVbs'
bot = telebot.TeleBot(token)
#491160995:AAFFB7Y6R60-kCc3Bcs0wVKDPXhpoNM18bQ
@bot.message_handler()
def msgUser(message):
    #print(message.chat.id, message.chat.first_name, message.chat.last_name, message.chat.text)
    add_user(message.chat.first_name, message.chat.last_name, message.text,message.chat.id)
    bot.send_message(message.chat.id, 'Hello'+message.chat.first_name)
bot.polling(none_stop=True)


if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 7775,
        'engine.autoreload.on': False
    })
    cherrypy.quickstart(WebhookServer(), '/', {'/': {}})
