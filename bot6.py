#!/usr/bin/env python3
import cherrypy

import telebot
import time
import json
import simple_game1

BOT_TOKEN = '450087644:AAHREmBtANmyRbDu4uxVc3I7tK--L0qcVbs'

bot = telebot.TeleBot(BOT_TOKEN)

# Хэндлер на все текстовые сообщения
@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    #add_user(message.chat.first_name, message.chat.last_name, message.text, message.chat.id)
    bot.send_message(message.chat.id, 'Hello' + message.chat.first_name)

class WebhookServer(object):
    # index равнозначно /, т.к. отсутствию части после ip-адреса (грубо говоря)
    @cherrypy.expose
    def index(self):
        length = int(cherrypy.request.headers['content-length'])
        json_string = cherrypy.request.body.read(length).decode("utf-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''

if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 7771,
        'engine.autoreload.on': False
    })
    cherrypy.quickstart(WebhookServer(), '/', {'/': {}})
