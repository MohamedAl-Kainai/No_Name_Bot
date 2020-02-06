#! /usr/bin/python3
import telebot,json

def GetData(file,searsh=[]):
    with open(f'db/{file}.json') as x:
        DATA = json.load(x)
    for i in searsh:
        DATA = DATA[i]
    return DATA
