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
    if not type(word) is str:
        return "error int"
    if not word.isalpha():
        return "error alph"
    for w in word: 
        if w in alph:
            ind = alph.index(w)
        else:
            return "error"
        s += alph[ind - step]
    return s

def code1(text = "asdfgh", step = 1):
    global alph
    alph = [chr(i) for i in range(ord('a'), ord('z'))]
    return decoding(text, step)


@bot.message_handler(commands = ['start'])
def url(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Caesar cipher")
    btn2 = types.KeyboardButton('---')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "choose code", reply_markup=markup)


@bot.message_handler(commands=['code1'])
def start(message):
    pass
   

@bot.message_handler(content_types=['text'])
def choose_code(message):
    global name_code
    if name_code == "ans_Caesar":
        inf_code = message.text.split()
        if not len(inf_code) == 2:
            bot.send_message(message.from_user.id, "error")
        else:
            bot.send_message(message.from_user.id, code1(inf_code[0], int(inf_code[1])), parse_mode='Markdown')
            name_code = None
            mes = ""
    if message.text == "Caesar cipher":
        bot.send_message(message.from_user.id, "enter mes and step. Exemple: abc 2")
        name_code = "ans_Caesar"
    

name_code = None
bot.polling(none_stop=True, interval=0) 