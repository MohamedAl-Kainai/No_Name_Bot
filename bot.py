#! /usr/bin/python3
import telebot ,time ,os ,random
from telebot import types
from db import db
from SERVICES import No_Name

# Input user...
TOKEN = 'Token..'
No_Name.NameGroup = 'group name'
No_Name.UrlGroup = 'group url'

# bot token
bot = telebot.TeleBot(token=TOKEN)
tb = telebot.AsyncTeleBot(TOKEN)

# start_command...---------------------
@bot.message_handler(commands=['start'])
def start_command(message):
    m = 'ماذا يقدمة هذا البوت؟ \n\nالبوت في تطور مستمر ان شاء الله عند الأنتهاء منه سوف يغطي اكبر عدد ممكن من الخدمات من دورات معلومات اجابه عن اسأله وغيرها...'
    if message.chat.type == 'private':
        bot.send_message(chat_id=message.chat.id,text=m,reply_markup=No_Name.start_command(None,bot).Intro(),parse_mode='HTML')

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    No_Name.start_command(call,bot).Call()
# End start_command...------------------

@bot.message_handler(func=lambda m: True)
def Read_messages(message):
    # help
    if No_Name.get_list(message):
        bot.reply_to(message,No_Name.get_list(message),parse_mode='Markdown')

bot.polling(none_stop=True)
