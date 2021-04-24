import sys

import telebot
from kaleidoscope import PhotoFilters

TOKEN = "1703000496:AAHm-ZCPVAp_T5eZ4ygyNewfXKUvqnKX3Ww"
bot = telebot.TeleBot(TOKEN)

effect = 'Sepia'
advanced_settings = ''


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Choose filter and send me a photo.")


@bot.message_handler(commands=['effects'])
def pick_the_effect(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Sepia', 'Negative', 'Contrast')
    keyboard.row('Gray_Scale', 'White_Black', 'Bright')
    keyboard.row('Emboss', 'Contour', 'Edges')
    keyboard.row('Brannan', 'Brooklyn', 'Clarendon')
    keyboard.row('Css', 'Earlybird', 'Gingham')
    keyboard.row('Hudson', 'Inkwell', 'Kelvin')
    keyboard.row('Lark', 'Lofi', 'Maven')
    keyboard.row('Mayfair', 'Moon', 'Nashville')
    keyboard.row('Perpetua', 'Reyes', 'Rise')
    keyboard.row('Slumber', 'Stinson', 'Toaster')
    keyboard.row('Util', 'Valencia', 'Walden')
    keyboard.row('Willow', 'Xpro2', 'Aden')
    bot.send_message(message.chat.id, 'Got it', reply_markup=keyboard)  # WIRED


@bot.message_handler(commands=['advanced'])
def advanced(message):
    pass  # change brightness and coefficient


@bot.message_handler(content_types=["text"])
def picked_effect(message):
    global effect
    effect = message.text


@bot.message_handler(content_types=["photo"])
def beauty(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = '../data/Photo.jpg'

    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)

    eval(f"PhotoFilters().{effect.lower()}('../data/Photo.jpg', '../data/ResultPhoto.jpg')")

    photo = open('../data/ResultPhoto.jpg', 'rb')

    bot.send_message(message.chat.id, 'Фото добавлено')
    bot.send_photo(message.chat.id, photo)


bot.polling()
