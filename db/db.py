#! /usr/bin/python3
import telebot,json

def GetData(file,searsh=[]):
    with open(f'db/{file}.json') as x:
        DATA = json.load(x)
    for i in searsh:
        DATA = DATA[i]
    return DATA

# x = {'chat':{'markup':{'program_coursesMSG':'افضل دورات لأشهر لغات البرمجة المشهوره... \U0001f601'}}}
# with open('chat.json','w')as f:
#     f.write(json.dumps(x,indent='2'))
