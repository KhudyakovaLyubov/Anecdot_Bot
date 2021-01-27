import telebot

f = open('token.txt').read()
bot = telebot.TeleBot(f)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет', 'Пока')

keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('Да', 'Нет')

keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('Меню', 'Справка')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я твой Бот_Анекдот!', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока, мой создатель')

@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    id = message.sticker.file_id
    bot.send_sticker(message.chat.id, id)

bot.polling()
