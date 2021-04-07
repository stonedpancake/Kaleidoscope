import sys

import telebot
from kaleidoscope import PhotoFilters

TOKEN = "1703000496:AAHm-ZCPVAp_T5eZ4ygyNewfXKUvqnKX3Ww"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=["photo"])
def beauty(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    downloaded_file_name = 'Loki.jpg'
    src = '/Users/slavaderebchinskiy/Documents/python/Kaleidoscope/data/' + downloaded_file_name

    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
        new_file_name = 'res1.jpg'
        PhotoFilters().white_black('../data/' + downloaded_file_name, '../data/' + new_file_name, 1.2)

    photo = open('../data/' + new_file_name, 'rb')
    bot.reply_to(message, "Фото добавлено")
    bot.send_photo(message.chat.id, photo)


bot.polling()
