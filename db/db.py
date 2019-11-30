#! /usr/bin/python3

import telebot
from db import DATA

TOKEN = '804290219:AAGmXyBRylifh6RYqkpynnfW8DHW3aV0Muo'
bot = telebot.TeleBot(token=TOKEN)

class data:
    def __init__(self,message,type='Save_Data'):
        self.type = type
        self.message = message
        run = {
        'Save_Data':self.Save_Data,
        'Add_Data':self.Add_Data,
        }
        run[type]()

    def Save_Data(self):
        Data = '''all_users_info = {}
all_admin_info = {}
all_private_info = {}
all_supergroup_info = {}
all_group_info = {}
        '''.format(
        DATA.all_users_info,
        DATA.all_admin_info,
        DATA.all_private_info,
        DATA.all_supergroup_info,
        DATA.all_group_info,
        ).replace(
        '= {','= {\n'
        ).replace(
        '}, ','},\n'
        ).replace(
        '}}','}\n}\n'
        )
        with open('db/DATA.py','w') as db:
            db.write(str(Data))

    def Add_Data(self):
        message = self.message
        # all_users
        DATA.all_users_info[message.from_user.id] = {
        'id':message.from_user.id,
        'group_id':message.chat.id,
        'is_bot':message.from_user.is_bot,
        'first_name':message.from_user.first_name,
        'last_name':message.from_user.last_name,
        'username':message.from_user.username,
        }
        # all creators and admins
        if 'creator' == bot.get_chat_member(message.chat.id,message.from_user.id).status:
            DATA.all_admin_info[message.from_user.id] = {
            'is_creator':True,
            'group_id':message.chat.id,
            'type':message.chat.type,
            'group_name':message.chat.username,
            'id':message.from_user.id,
            'is_bot':message.from_user.is_bot,
            'first_name':message.from_user.first_name,
            'last_name':message.from_user.last_name,
            'username':message.from_user.username,
            }
        elif 'administrator' == bot.get_chat_member(message.chat.id,message.from_user.id).status:
            DATA.all_admin_info[message.from_user.id] = {
            'is_creator':False,
            'group_id':message.chat.id,
            'type':message.chat.type,
            'group_name':message.chat.username,
            'id':message.from_user.id,
            'is_bot':message.from_user.is_bot,
            'first_name':message.from_user.first_name,
            'last_name':message.from_user.last_name,
            'username':message.from_user.username,
            }
        # all private users
        if 'private' == message.chat.type:
            DATA.all_private_info[message.chat.id] = {
            'id':message.chat.id,
            'first_name':message.from_user.first_name,
            'last_name':message.from_user.last_name,
            'username':message.from_user.username,
            }
        # all supergroup
        if 'supergroup' == message.chat.type:
            DATA.all_supergroup_info[message.chat.id] = {
            'chat_id':message.chat.id,
            'username':message.chat.username,
            }
        # all group
        if 'group' == message.chat.type:
            DATA.all_group_info[message.chat.id] = {
            'chat_id':message.chat.id,
            'username':message.chat.username,
            }

def check_admin(message):
    if message.from_user.id in DATA.all_admin_info:
        if DATA.all_admin_info[message.from_user.id]['group_id'] == message.chat.id:
            return True
    else:
        return False
