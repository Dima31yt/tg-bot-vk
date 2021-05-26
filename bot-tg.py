## -*- coding: utf-8 -*-
import telebot, vk_api

token = "1720175651:AAGQePH6EBc1LD81ogaMbZE0ELkNCukGuRA"
bot = telebot.TeleBot(token)

vk_session = vk_api.VkApi(token="eafd22df108f95d1449ab77635650aa878d089231eb5ce40c09ac6e01ddbdbef5948c6c173abc886c01ca")
vk = vk_session.get_api()

@bot.message_handler(commands=['start', 'help'])  
def help_command(message):
    alert_keyboard = telebot.types.InlineKeyboardMarkup()  
    alert_keyboard.add(telebot.types.InlineKeyboardButton("Оповестить собеседника", callback_data='alert'))

    bot.send_message(
        message.chat.id,
        'Диалог начат',
        reply_markup=alert_keyboard
    )

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.chat.id)
    msg = message.text
    vk.messages.send(user_id=400484262, message=msg, random_id=0)

bot.polling(none_stop=True)