import telebot

f = open('token.txt').read()
bot = telebot.TeleBot(f)

keyboardHello = telebot.types.ReplyKeyboardMarkup()
keyboardHello.row('Меню', 'Справка')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я твой Бот_Анекдот!', reply_markup=keyboardHello)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой гость!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока, мой гость!')
    elif message.text.lower() == 'Меню':
        bot.send_message(message.chat.id, 'Выбери раздел:')

@bot.message_handler(content_types=['text'])
def send_user_info(message):
    if message.text.lower() == 'Информация о пользователе':
        bot.send_message(message.chat.id, 'Выбери поле:')
    elif message.text.lower() == 'Имя':
        bot.send_message(message.chat.id, message.chat.first_name)
    elif message.text.lower() == 'ID':
        bot.send_message(message.chat.id, message.chat.id)
    elif message.text.lower() == 'Фамилия':
        bot.send_message(message.chat.id, message.chat.last_name)
    elif message.text.lower() == 'Логин':
        bot.send_message(message.chat.id, message.chat.username)
    elif message.text.lower() == 'Тип профиля':
        bot.send_message(message.chat.id, message.chat.type)

@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    id = message.sticker.file_id
    bot.send_sticker(message.chat.id, id)

bot.polling()
