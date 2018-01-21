#!/usr/bin/env python3

import cherrypy
import requests
import telebot

WEBHOOK_HOST = '139.59.146.78'
WEBHOOK_PORT = 443  # 443, 80, 88 или 8443
WEBHOOK_LISTEN = '0.0.0.0' # Слушаем отовсюду
WEBHOOK_SSL_CERT = 'webhook_cert.pem'  # Путь к сертификату
WEBHOOK_SSL_PRIV = 'webhook_pkey.pem'  # Путь к закрытому ключу
WEBHOOK_URL_BASE = "https://{!s}:{!s}".format(WEBHOOK_HOST, WEBHOOK_PORT)

BOT_1_TOKEN = '450087644:AAHREmBtANmyRbDu4uxVc3I7tK--L0qcVbs'
# BOT_2_TOKEN = ""
# BOT_3_TOKEN = ""
# BOT_4_TOKEN = ""
# BOT_5_TOKEN = ''
# BOT_6_TOKEN = ''
# BOT_7_TOKEN = ''

# Вводим здесь IP-адреса и порты, куда перенаправлять входящие запросы.
# Т.к. всё на одной машине, то используем локалхост + какие-нибудь свободные порты.
# https в данном случае не нужен, шифровать незачем.
BOT_1_ADDRESS = "http://127.0.0.1:7771"
# BOT_2_ADDRESS = "http://127.0.0.1:7772"
# BOT_3_ADDRESS = "http://127.0.0.1:7773"
# BOT_4_ADDRESS = "http://127.0.0.1:7774"
# BOT_5_ADDRESS = "http://127.0.0.1:7775"
# BOT_6_ADDRESS = "http://127.0.0.1:7776"
# BOT_7_ADDRESS = "http://127.0.0.1:7777"

bot_1 = telebot.TeleBot(BOT_1_TOKEN)
# bot_2 = telebot.TeleBot(BOT_2_TOKEN)
# # bot_3 = telebot.TeleBot(BOT_3_TOKEN)
# bot_4 = telebot.TeleBot(BOT_4_TOKEN)
# bot_5 = telebot.TeleBot(BOT_5_TOKEN)
# bot_6 = telebot.TeleBot(BOT_6_TOKEN)
# bot_7 = telebot.TeleBot(BOT_7_TOKEN)

# Описываем наш сервер
class WebhookServer(object):

    # Первый бот (название функции = последняя часть URL вебхука)
    @cherrypy.expose
    def AAAA(self):
        if 'content-length' in cherrypy.request.headers and \
           'content-type' in cherrypy.request.headers and \
           cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            # Вот эта строчка и пересылает все входящие сообщения на нужного бота
            requests.post(BOT_1_ADDRESS, data=json_string)
            return ''
        else:
            raise cherrypy.HTTPError(403)

    # Второй бот (действуем аналогично)
    # @cherrypy.expose
    # def ZZZZ(self):
    #     if 'content-length' in cherrypy.request.headers and \
    #        'content-type' in cherrypy.request.headers and \
    #        cherrypy.request.headers['content-type'] == 'application/json':
    #         length = int(cherrypy.request.headers['content-length'])
    #         json_string = cherrypy.request.body.read(length).decode("utf-8")
    #         requests.post(BOT_2_ADDRESS, data=json_string)
    #         return ''
    #     else:
    #         raise cherrypy.HTTPError(403)
    #
    # # # cDemon
    # # @cherrypy.expose
    # # def XXXX(self):
    # #     if 'content-length' in cherrypy.request.headers and \
    # #        'content-type' in cherrypy.request.headers and \
    # #        cherrypy.request.headers['content-type'] == 'application/json':
    # #         length = int(cherrypy.request.headers['content-length'])
    # #         json_string = cherrypy.request.body.read(length).decode("utf-8")
    # #         requests.post(BOT_3_ADDRESS, data=json_string)
    # #         return ''
    # #     else:
    # #         raise cherrypy.HTTPError(403)
    #
    # # Четвертый бот (действуем аналогично) (Memory)
    # @cherrypy.expose
    # def YYYY(self):
    #     if 'content-length' in cherrypy.request.headers and \
    #        'content-type' in cherrypy.request.headers and \
    #        cherrypy.request.headers['content-type'] == 'application/json':
    #         length = int(cherrypy.request.headers['content-length'])
    #         json_string = cherrypy.request.body.read(length).decode("utf-8")
    #         requests.post(BOT_4_ADDRESS, data=json_string)
    #         return ''
    #     else:
    #         raise cherrypy.HTTPError(403)
    #
    # # (game)
    # @cherrypy.expose
    # def CCCC(self):
    #     if 'content-length' in cherrypy.request.headers and \
    #        'content-type' in cherrypy.request.headers and \
    #        cherrypy.request.headers['content-type'] == 'application/json':
    #         length = int(cherrypy.request.headers['content-length'])
    #         json_string = cherrypy.request.body.read(length).decode("utf-8")
    #         requests.post(BOT_5_ADDRESS, data=json_string)
    #         return ''
    #     else:
    #         raise cherrypy.HTTPError(403)
    #
    # # (game_dev)
    # @cherrypy.expose
    # def DDDD(self):
    #     if 'content-length' in cherrypy.request.headers and \
    #        'content-type' in cherrypy.request.headers and \
    #        cherrypy.request.headers['content-type'] == 'application/json':
    #         length = int(cherrypy.request.headers['content-length'])
    #         json_string = cherrypy.request.body.read(length).decode("utf-8")
    #         requests.post(BOT_6_ADDRESS, data=json_string)
    #         return ''
    #     else:
    #         raise cherrypy.HTTPError(403)
    #
    # # (poroshki_game)
    # @cherrypy.expose
    # def EEEE(self):
    #     if 'content-length' in cherrypy.request.headers and \
    #        'content-type' in cherrypy.request.headers and \
    #        cherrypy.request.headers['content-type'] == 'application/json':
    #         length = int(cherrypy.request.headers['content-length'])
    #         json_string = cherrypy.request.body.read(length).decode("utf-8")
    #         requests.post(BOT_7_ADDRESS, data=json_string)
    #         return ''
    #     else:
    #         raise cherrypy.HTTPError(403)


if __name__ == '__main__':

    bot_1.remove_webhook()
    bot_1.set_webhook(url='https://139.59.146.78/AAAA',
                    certificate=open(WEBHOOK_SSL_CERT, 'r'))

    # bot_2.remove_webhook()
    # bot_2.set_webhook(url='https://139.59.146.78/ZZZZ',
    #                 certificate=open(WEBHOOK_SSL_CERT, 'r'))
    #
    # # bot_3.remove_webhook()
    # # bot_3.set_webhook(url='https://139.59.146.78/XXXX',
    # #                 certificate=open(WEBHOOK_SSL_CERT, 'r'))
    #
    # bot_4.remove_webhook()
    # bot_4.set_webhook(url='https://139.59.146.78/YYYY',
    #                 certificate=open(WEBHOOK_SSL_CERT, 'r'))
    #
    # bot_5.remove_webhook()
    # bot_5.set_webhook(url='https://139.59.146.78/CCCC',
    #                 certificate=open(WEBHOOK_SSL_CERT, 'r'))
    #
    # bot_6.remove_webhook()
    # bot_6.set_webhook(url='https://139.59.146.78/DDDD',
    #                 certificate=open(WEBHOOK_SSL_CERT, 'r'))
    # bot_7.remove_webhook()
    # bot_7.set_webhook(url='https://139.59.146.78/EEEE',
    #                 certificate=open(WEBHOOK_SSL_CERT, 'r'))

    cherrypy.config.update({
        'server.socket_host': WEBHOOK_LISTEN,
        'server.socket_port': WEBHOOK_PORT,
        'server.ssl_module': 'builtin',
        'server.ssl_certificate': WEBHOOK_SSL_CERT,
        'server.ssl_private_key': WEBHOOK_SSL_PRIV,
        'engine.autoreload.on': False
    })
    cherrypy.quickstart(WebhookServer(), '/', {'/': {}})
