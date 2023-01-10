import telebot
import requests

bot = telebot.TeleBot("")


@bot.message_handler(commands=['currency'])
def send_welcome(message):
    msg = message.text
    items = msg.split()
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    bot.send_message(message.chat.id, f"{res['Valute'][items[1]]['Name']}, {res['Valute'][items[1]]['Value']}")


bot.infinity_polling()
