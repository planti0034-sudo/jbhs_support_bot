import os
import telebot
import types

BOT_TOKEN = "7066297556:AAEen9OWKQ0qU9TSUGESfPrzRuseNo6GrOE"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'помощь', 'help'])
def send_welcome(message):
    bot.reply_to(message, "👋🏻Здравствуйте, это оффициальный бот поддержки Токмокского лицея имени Ж.Баласагына. \n     Базовые команды: \n           /help или /помощь -- Показать это сообщение✔ \n          /price или /цена -- показать актуальную цену контракта💵\n           /faq или /ЧаВо -- Часто задаваемые вопросы и ответы на них❔\n          /site или /сайт -- ссылка на сайт лицея📳")

@bot.message_handler(commands=['price', 'цена'])
def price(message):
    bot.reply_to(message, "💵Актуальные цены контракта: \n       🧑🏻Начальная школа: 2000$ \n       👨🏻‍🦱Старшая школа: 3200$")

@bot.message_handler(commands=['сайт', 'site'])
def site(message):
    bot.reply_to(message, "Сайт лицея: https://tokmoksapat.edu.kg/")
    
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, "Я не знаю такую команду, напишите /help или /помощь что-бы вывести все доступные команды.")


bot.infinity_polling()