#! /usr/bin/python3

def get_list(message):
    if '#List' in message.text:
        text = message.text
        text = text.replace('#List\n','')
        text = text.replace('\n#List','')
        text = text.replace('#List','')
        text = text.replace('\n',' ')
        text = text.split(' ')
        return f'{text}'
    else:
        return False
