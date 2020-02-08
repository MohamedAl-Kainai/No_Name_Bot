#! /usr/bin/python3
import telebot,json

def GetData(file,searsh=[]):
    with open(f'db/{file}.json') as x:
        DATA = json.load(x)
    for i in searsh:
        DATA = DATA[i]
    return DATA

def AddData(file,data,searsh=[]):
    with open(f'db/{file}.json') as x:
        DATA = json.load(x)
    DATA['port'] = []
    return json.dumps(DATA,indent='  ')
