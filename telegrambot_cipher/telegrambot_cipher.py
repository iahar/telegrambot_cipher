import telebot
from telebot import types


bot = telebot.TeleBot('6096406269:AAFOHsTik7CxxSRxXXFE-sktzsHu8IXhceQ')


def coding(word, step):
    text_encoded = ''
    for w in word: 
        if w in alph:
            ind = alph.index(w)
        if w == ' ':
            text_encoded += ' '
        elif ind + step < 33:
            text_encoded += alph[ind + step]
        else:
            text_encoded += alph[32 - ind]
    return text_encoded

def decoding(word, step):
    s = ''
    for w in word: 
        if w in alph:
            ind = alph.index(w)
        else:
            return "error alph"
        if ind + int(step%23) > 23:
            s += alph[23 - ind + int(step%23)]
        else:
            s += alph[ind + int(step%23)]
    return s

def code1(text = "asdfgh", step = 1):
    global alph
    alph = [chr(i) for i in range(ord('a'), ord('z')+1)]
    return decoding(text, step)


@bot.message_handler(commands = ['start'])
def url(message):
    bot.send_message(message.from_user.id, "choose code: /caesar_cipher /2")


@bot.message_handler(commands=['caesar_cipher'])
def caesar(message):
    global name_code
    bot.send_message(message.from_user.id, "enter mes and step. Exemple: abc 2")
    name_code = "caesar_cipher"


@bot.message_handler(commands=['2'])
def f2(message):
    global name_code
    bot.send_message(message.from_user.id, "----")
    name_code = "2"


@bot.message_handler(commands=['buy'])
def end(message):
    bot.send_message(message.from_user.id, "good night :)")
    
   
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global name_code
    inf_code = message.text.split()
    if name_code == "caesar_cipher":
        if not len(inf_code) == 2:
            bot.send_message(message.from_user.id, "error info")
        else:
            bot.send_message(message.from_user.id, code1(inf_code[0], int(inf_code[1])), parse_mode='Markdown')
    if name_code == "2":
        bot.send_message(message.from_user.id, inf_code[0], parse_mode='Markdown')
    name_code = None

    

name_code = None
bot.polling(none_stop=True, interval=0) 