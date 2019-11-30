#! /usr/bin/python3
import re

def check_url(message):
    text = message.text
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)
    try:
        if urls[0] in text:
            return True
    except:
        return False
def Bad_Words(message):
    Bad_Words = [
    ' كس ',' زبي ',' يا كلب',' عرص ',
    ' انيكك ',' يا ابن الوسخه',' زنوه ',
    ' قحبة ',' شرموط ',' شرموطة ',' يا ابن',
    ' لوطي ',' حيوان ',' خرا ',' سامج ',' تافه ',
    ' انا اندعك',' انا انيكك',' كلب',
    ]
    for bad in Bad_Words:
        if bad in message.text:
            return True
            break
    else:
        return False
