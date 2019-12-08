from telebot import types

class check:
    def __init__(self,args):
        self.args = args

    def clear(self,text=False):
        return self.args.format(text).replace('@','').replace('None','').replace('http','').replace('/','').replace(':','') if text else self.args.replace('@','').replace('None','').replace('http','').replace('/','').replace(':','')

class start_command:
    def __init__(self,call,bot):
        self.call = call
        self.bot = bot

    def Intro(self):
        markup = types.InlineKeyboardMarkup()
        markup.row(types.InlineKeyboardButton('< No_Name >', url='https://t.me/joinchat/AAAAAFBqSAHafemT3Twrkg'))
        markup.add(types.InlineKeyboardButton(text='•⊱  الخدمات  ⊰•',callback_data='services'))
        markup.row(types.InlineKeyboardButton(text='•⊱   المطور   ⊰•', url='https://t.me/ThE_GhOsT_404'))
        return markup

    def services(self):
        markup = types.InlineKeyboardMarkup()
        markup.row(types.InlineKeyboardButton('< No_Name >', url='https://t.me/joinchat/AAAAAFBqSAHafemT3Twrkg'))
        markup.add(types.InlineKeyboardButton(text='•⊱  تعلم لغات البرمجة ⊰•',callback_data='programming_courses'))
        markup.add(types.InlineKeyboardButton(text='•⊱  دوراة السكيورتي ⊰•',callback_data='hack_courses'))
        markup.add(types.InlineKeyboardButton(text='•⊱  تقنية & برمجة & سكيورتي ⊰•',callback_data='courses'))
        markup.add(types.InlineKeyboardButton(text='رجوع',callback_data='back_intro'))
        return markup

    def programming_courses(self):
        program_courses = {
        'Python':['https://t.me/joinchat/AAAAAFBqSAHafemT3Twrkg'],
        'java':['https://t.me/joinchat/AAAAAFBqSAHafemT3Twrkg'],
        'C#':['https://t.me/joinchat/AAAAAFBqSAHafemT3Twrkg'],
        'Html':['https://t.me/joinchat/AAAAAFBqSAHafemT3Twrkg'],
        'CSS':['https://t.me/joinchat/AAAAAFBqSAHafemT3Twrkg'],
        'JavaScript':['https://t.me/joinchat/AAAAAFBqSAHafemT3Twrkg'],
        'Sql':['https://t.me/joinchat/AAAAAFBqSAHafemT3Twrkg'],
        'php':['https://t.me/joinchat/AAAAAFBqSAHafemT3Twrkg'],
        'None':['https://t.me/joinchat/AAAAAFBqSAHafemT3Twrkg'],
        'None1':['https://t.me/joinchat/AAAAAFBqSAHafemT3Twrkg'],
        'None2':['https://t.me/joinchat/AAAAAFBqSAHafemT3Twrkg'],
        'None3':['https://t.me/joinchat/AAAAAFBqSAHafemT3Twrkg'],
        'None4':['https://t.me/joinchat/AAAAAFBqSAHafemT3Twrkg'],
        'None5':['https://t.me/joinchat/AAAAAFBqSAHafemT3Twrkg'],
        'None6':['https://t.me/joinchat/AAAAAFBqSAHafemT3Twrkg'],
        'None7':['https://t.me/joinchat/AAAAAFBqSAHafemT3Twrkg'],

        }
        x = [i for i in program_courses.keys()]
        y = program_courses
        markup = types.InlineKeyboardMarkup()
        Button = types.InlineKeyboardButton
        markup.row(Button('< No_Name >', url='https://t.me/joinchat/AAAAAFBqSAHafemT3Twrkg'))
        markup.row(Button(text=x[0], url=y[x[0]][0]),Button(text=x[1], url=y[x[1]][0]),Button(text=x[2], url=y[x[2]][0]))
        markup.row(Button(text=x[3], url=y[x[3]][0]),Button(text=x[4], url=y[x[4]][0]),Button(text=x[5], url=y[x[5]][0]))
        markup.row(Button(text=x[6], url=y[x[6]][0]),Button(text=x[7], url=y[x[7]][0]),Button(text=x[8], url=y[x[8]][0]))
        markup.row(Button(text=x[9], url=y[x[9]][0]),Button(text=x[10], url=y[x[10]][0]),Button(text=x[11], url=y[x[11]][0]))
        markup.row(Button(text=x[9], url=y[x[9]][0]),Button(text=x[10], url=y[x[10]][0]),Button(text=x[11], url=y[x[11]][0]))
        markup.row(Button(text=x[9], url=y[x[9]][0]),Button(text=x[10], url=y[x[10]][0]),Button(text=x[11], url=y[x[11]][0]))
        markup.row(Button(text=x[9], url=y[x[9]][0]),Button(text=x[10], url=y[x[10]][0]),Button(text=x[11], url=y[x[11]][0]))
        markup.row(Button(text=x[9], url=y[x[9]][0]),Button(text=x[10], url=y[x[10]][0]),Button(text=x[11], url=y[x[11]][0]))
        markup.row(Button(text=x[9], url=y[x[9]][0]),Button(text=x[10], url=y[x[10]][0]),Button(text=x[11], url=y[x[11]][0]))
        markup.add(Button(text='•⊱  ملاحظة  ⊰•',callback_data='send_note'))
        markup.add(Button(text='رجوع',callback_data='back_services'))
        return markup

    def Call(self):
        call = self.call
        bot = self.bot
        m = 'ماذا يقدمة هذا البوت؟ \n\nالبوت في تطور مستمر ان شاء الله عند الأنتهاء منه سوف يغطي اكبر عدد ممكن من الخدمات من دورات معلومات اجابه عن اسأله وغيرها...'
        if call.data.startswith('services'):
            bot.edit_message_text(chat_id=call.message.chat.id,text=m,message_id=call.message.message_id,reply_markup=self.services(),parse_mode='HTML')
        if call.data.startswith('back_intro'):
            bot.edit_message_text(chat_id=call.message.chat.id,text=m,message_id=call.message.message_id,reply_markup=self.Intro(),parse_mode='HTML')
        if call.data.startswith('programming_courses'):
            bot.edit_message_text(chat_id=call.message.chat.id,text=m,message_id=call.message.message_id,reply_markup=self.programming_courses(),parse_mode='HTML')
        if call.data.startswith('back_services'):
            bot.edit_message_text(chat_id=call.message.chat.id,text=m,message_id=call.message.message_id,reply_markup=self.services(),parse_mode='HTML')
        if call.data.startswith('send_note'):
            bot.answer_callback_query(call.id,show_alert=True,text='في كل مره يتم عرض دورة مختلفه',)
