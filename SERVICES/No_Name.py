from telebot import types
import random, json
from db import db

UrlGroup = ''
NameGroup = ''
class start_command:
    def __init__(self,call,bot,message):
        self.call = call
        self.bot = bot
        self.message = message

        if message != None:
            if self.message.chat.type == 'private':
                m = 'ماذا يقدمة هذا البوت؟ \n\nالبوت في تطور مستمر ان شاء الله عند الأنتهاء منه سوف يغطي اكبر عدد ممكن من الخدمات من دورات معلومات اجابه عن اسأله وغيرها...'
                bot.send_message(chat_id=message.chat.id,text=m,reply_markup=self.Intro(),parse_mode='HTML')

    def Intro(self):
        markup = types.InlineKeyboardMarkup()
        markup.row(types.InlineKeyboardButton(NameGroup, url=UrlGroup))
        markup.add(types.InlineKeyboardButton(text='•⊱  الخدمات  ⊰•',callback_data='services'))
        markup.row(types.InlineKeyboardButton(text='•⊱   المطور   ⊰•', url='https://t.me/ThE_GhOsT_404'))
        return markup

    def services(self):
        markup = types.InlineKeyboardMarkup()
        markup.row(types.InlineKeyboardButton(NameGroup, url=UrlGroup))
        markup.add(types.InlineKeyboardButton(text='•⊱  تعلم لغات البرمجة ⊰•',callback_data='programming_courses'))
        markup.add(types.InlineKeyboardButton(text='•⊱  دوراة السكيورتي ⊰•',callback_data='hack_courses'))
        markup.add(types.InlineKeyboardButton(text='•⊱  تقنية & برمجة & سكيورتي ⊰•',callback_data='courses'))
        markup.add(types.InlineKeyboardButton(text='رجوع',callback_data='back_intro'))
        return markup

    def programming_courses(self):
        U = self.RandUrl
        data = db.GetData('web',searsh=['urls','program_courses'])
        program_courses = {
        'Python':U(data['Python']),
        'Java':U(data['Java']),
        'C#':U(data['C#']),
        'Html':U(data['Html']),
        'CSS':U(data['CSS']),
        'JavaScript':U(data['JavaScript']),
        'Sql':U(data['Sql']),
        'php':U(data['php']),
        'C':U(data['C']),
        'Kotlin':U(data['Kotlin']),
        'C++':U(data['C++']),
        'Ruby':U(data['Ruby']),
        'Bash':U(data['Bash']),
        'Swift':U(data['Swift']),
        'Visual':U(data['Visual']),}

        x = [i for i in program_courses.keys()]
        y = program_courses
        markup = types.InlineKeyboardMarkup()
        Button = types.InlineKeyboardButton
        markup.row(Button(NameGroup, url=UrlGroup))
        markup.row(Button(text=x[0], url=y[x[0]]),Button(text=x[1], url=y[x[1]]),Button(text=x[2], url=y[x[2]]))
        markup.row(Button(text=x[3], url=y[x[3]]),Button(text=x[4], url=y[x[4]]),Button(text=x[5], url=y[x[5]]))
        markup.row(Button(text=x[6], url=y[x[6]]),Button(text=x[7], url=y[x[7]]),Button(text=x[8], url=y[x[8]]))
        markup.row(Button(text=x[9], url=y[x[9]]),Button(text=x[10], url=y[x[10]]),Button(text=x[11], url=y[x[11]]))
        markup.row(Button(text=x[12], url=y[x[12]]),Button(text=x[13], url=y[x[13]]),Button(text=x[14], url=y[x[14]]))
        markup.add(Button(text='•⊱  تحديث  ⊰•',callback_data='update1'))
        markup.add(Button(text='•⊱  ملاحظة  ⊰•',callback_data='send_note'))
        markup.add(Button(text='رجوع',callback_data='back_services'))
        return markup

    def RandUrl(self,list_text):
        rand = random.randint(0,len(list_text)-1)
        return list_text[rand]

    def Call(self):
        call = self.call
        bot = self.bot
        PC = db.GetData('chat',searsh=['chat','markup','program_coursesMSG'])
        m = 'ماذا يقدمة هذا البوت؟ \n\nالبوت في تطور مستمر ان شاء الله عند الأنتهاء منه سوف يغطي اكبر عدد ممكن من الخدمات من دورات معلومات اجابه عن اسأله وغيرها...'
        if call.data.startswith('services'):
            bot.edit_message_text(chat_id=call.message.chat.id,text=m,message_id=call.message.message_id,reply_markup=self.services(),parse_mode='HTML')
        if call.data.startswith('back_intro'):
            bot.edit_message_text(chat_id=call.message.chat.id,text=m,message_id=call.message.message_id,reply_markup=self.Intro(),parse_mode='HTML')
        if call.data.startswith('programming_courses'):
            bot.edit_message_text(chat_id=call.message.chat.id,text=PC,message_id=call.message.message_id,reply_markup=self.programming_courses(),parse_mode='HTML')
        if call.data.startswith('back_services'):
            bot.edit_message_text(chat_id=call.message.chat.id,text=m,message_id=call.message.message_id,reply_markup=self.services(),parse_mode='HTML')
        if call.data.startswith('send_note'):
            bot.answer_callback_query(call.id,show_alert=True,text='في كل مره يتم التحديث يتم عرض دورات مختلفة',)
        if call.data.startswith('update1'):
            bot.edit_message_text(chat_id=call.message.chat.id,text=PC,message_id=call.message.message_id,reply_markup=self.programming_courses(),parse_mode='HTML')

class Services:
    def __init__(self,bot,message):
        self.get_list(bot,message)
        self.get_json(bot,message)
        self.get_info(bot,message)

    def FindTextInChat(self,word,text):
        text = text.replace(word,'')
        text = text.replace('\n',' ')
        return text

    def get_list(self,bot,message):
        if '#List' in message.text:
            text = self.FindTextInChat('#List',message.text)
            text = text.split(' ')
            text = list(set(text))
            if '' in text:
                text.remove('')
            bot.reply_to(message,f'`{text}`',parse_mode='Markdown')

    def get_json(self,bot,message):
        if '#Json' in message.text:
            try:
                JS = eval(self.FindTextInChat('#Json',message.text))
                JS = json.dumps(JS,indent='  ')
                print (JS)
                bot.reply_to(message,f'`{JS}`',parse_mode='Markdown')
            except :
                bot.reply_to(message,'SyntaxError: invalid syntax',parse_mode='Markdown')

    def get_info(self,bot,message):
        if '#ME' in message.text:
            bot.reply_to(message,
            f"#Json...\nuser {json.dumps(eval(str(message.from_user)),indent='  ')}\nchat {json.dumps(eval(str(message.chat)),indent='  ')}",
            parse_mode='Markdown')
