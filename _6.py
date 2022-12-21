import telebot
import requests

bot = telebot.TeleBot('5618638676:AAF4va3Ae5gFPffeH9QAOr1i_TikhcKAces')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'привет, чтобы узнать, что может этот бот, напиши /help')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'этот бот присылает тебе твое случайное слово. чтобы попробовать, напиши /word и кликни по ссылке (она безопасна)')

@bot.message_handler(commands=['word'])
def wuf(message):
    r = requests.get('https://random-word-api.herokuapp.com/word')
    
    q = r.json()
    bot.send_message(message.chat.id, q)


bot.polling(none_stop=True)
