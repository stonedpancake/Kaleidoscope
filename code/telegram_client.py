import sys

import telebot
from kaleidoscope import PhotoFilters

TOKEN = "1703000496:AAHm-ZCPVAp_T5eZ4ygyNewfXKUvqnKX3Ww"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Howdy, how are you doing?")


@bot.message_handler(content_types=["photo"])
def beauty(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = '/Users/slavaderebchinskiy/Documents/python/Kaleidoscope/data/Photo.jpg'

    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)

    PhotoFilters().white_black('../data/Photo.jpg', '../data/ResultPhoto.jpg', 1.2)

    photo = open('../data/ResultPhoto.jpg', 'rb')

    bot.send_message(message.chat.id, 'Фото добавлено')
    bot.send_photo(message.chat.id, photo)


bot.polling()
