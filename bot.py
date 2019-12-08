#! /usr/bin/python3
import telebot ,time ,os ,random
from telebot import types
from db import db,DATA,send
from Riot import riot
from SERVICES import help_user ,Url ,No_Name
check = No_Name.check

# bot token
TOKEN = 'Token...'
bot = telebot.TeleBot(token=TOKEN)
tb = telebot.AsyncTeleBot(TOKEN)
admin_bot = [772949762]

def random_chat(list_text):
    rand = random.randint(0,len(list_text)-1)
    return list_text[rand]

@bot.message_handler(commands=['start'])
def start_command(message):
    m = 'ماذا يقدمة هذا البوت؟ \n\nالبوت في تطور مستمر ان شاء الله عند الأنتهاء منه سوف يغطي اكبر عدد ممكن من الخدمات من دورات معلومات اجابه عن اسأله وغيرها...'
    if message.chat.type == 'private':
        bot.send_message(chat_id=message.chat.id,text=m,reply_markup=No_Name.start_command(None,bot).Intro(),parse_mode='HTML')

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    No_Name.start_command(call,bot).Call()

@bot.message_handler(func=lambda m: True)
def Read_messages(message):
    chat_id ,message_id ,user_username ,user_id ,first_name,last_name= [
    message.chat.id ,
    message.message_id,
    message.from_user.username,
    message.from_user.id,
    message.from_user.first_name,
    message.from_user.last_name,
    ]
    # to save data...
    db.data(bot,message,type='Add_Data')
    db.data(bot,message,type='Save_Data')

    # Scan url...
    if message.chat.type == 'private':
        Url.Scan(message,TOKEN)
    elif user_id in admin_bot:
        Url.Scan(message,TOKEN)

    # to delete urls and bad words...
    try:
        if 'private' != message.chat.type:
            if not db.check_admin(message):
                if riot.check_url(message):
                    bot.delete_message(chat_id,message_id)
                elif riot.Bad_Words(message):
                    bot.delete_message(chat_id,message_id)
                    bot.send_message(chat_id,check(random_chat(send.message_bad_words)).clear(text=str(first_name)+str(last_name)))
    finally:
        os.system('clear')

    # help
    if help_user.get_list(message):
        bot.reply_to(message,help_user.get_list(message))

bot.polling(none_stop=True)
