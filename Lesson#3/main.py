import telebot
from config import *
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from random import randint

bot = telebot.TeleBot(TOKEN)
rand_nums = {}


def generate_num(chat_id):
    rand_nums[chat_id] = randint(1, 10)


@bot.message_handler(commands=['help', 'start'])
def handle_command(message):
    generate_num(message.chat.id)

    keyboard = ReplyKeyboardMarkup()
    # keyboard.add(KeyboardButton('Hello'), KeyboardButton('123'), KeyboardButton('321'), KeyboardButton('Hello'))

    buttons = []

    for i in range(10):
        buttons.append(KeyboardButton(str(i + 1)))

    keyboard.add(*buttons)
    bot.send_message(message.chat.id, 'Choose number', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def handle_message(message):
    chat_id = message.chat.id
    text = message.text

    if text.isdigit() and int(text) == rand_nums.get(chat_id):
        bot.send_message(chat_id, 'You guessed!! Try again!')
        generate_num(chat_id)

    else:
        bot.send_message(chat_id, 'Try again!')


if __name__ == '__main__':
    bot.polling(True)
