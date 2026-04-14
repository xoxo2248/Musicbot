import telebot
import requests
requests.packages.urllib3.util.connection.HAS_IPV6 = False

BOT_TOKEN = "8499197275:AAG2XIEjDiEB3UPnV1phGisaHItHUnd8YGc"
bot = telebot.TeleBot(BOT_TOKEN, threaded=False)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Music Bot Ready!")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "/play - song bajao")

bot.polling(none_stop=True, timeout=20)
