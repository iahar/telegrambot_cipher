﻿"""# -*- coding: utf-8 -*-"""
import telebot
from telebot import types

import ciphers.caesar
import ciphers.vigener
import ciphers.qwerty
import additional_functions.download_dictionary_words


bot = telebot.TeleBot('6228075641:AAH6aXTxj3tsAIPsiIN2RXt1tWjdzuVYUoE')
# test - 6096406269:AAFOHsTik7CxxSRxXXFE-sktzsHu8IXhceQ
# orig - 6228075641:AAH6aXTxj3tsAIPsiIN2RXt1tWjdzuVYUoE

@bot.message_handler(commands = ['start'])
def command_start(message):
    a = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 
                     "choose code: \n/decryption \n/caesar_code\n/caesar_decode \n/vigener_code макс-ная длина ключа для дешифровки 2\n/vigener_decode \n/qwerty", 
               reply_markup=a)


@bot.message_handler(commands=['caesar_code'])
def command_caesar(message):
    global name_code
    bot.send_message(message.from_user.id, "enter mes and step. Exemple: abc 2")
    name_code = "caesar_code"

@bot.message_handler(commands=['caesar_decode'])
def command_caesar(message):
    global name_code
    bot.send_message(message.from_user.id, "enter mes and step. Exemple: abc 2")
    name_code = "caesar_decode"

@bot.message_handler(commands=['vigener_code'])
def command_vigener(message):
    global name_code
    bot.send_message(message.from_user.id, "enter mes and key. Exemple: abc key")
    name_code = 'vigener_code'
    
@bot.message_handler(commands=['vigener_decode'])
def command_vigener(message):
    global name_code
    bot.send_message(message.from_user.id, "enter mes and key. Exemple: abc key")
    name_code = 'vigener_decode'

@bot.message_handler(commands=['qwerty'])
def command_vigener(message):
    global name_code
    bot.send_message(message.from_user.id, "enter mes")
    name_code = 'qwerty'


@bot.message_handler(commands=['decryption'])
def command_decryption(message):
    global name_code
    bot.send_message(message.from_user.id, "enter the message to decode")
    name_code = "decryption"

@bot.message_handler(commands=['buy'])
def command_end(message):
    bot.send_message(message.from_user.id, "good night :)")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global name_code

    inf_code = message.text.lower()
    arr_inf_code = inf_code.split()
    if name_code == "caesar_code":
        if len(arr_inf_code) < 2:
            bot.send_message(message.from_user.id, "error info")
        else:
            bot.send_message(message.from_user.id, ciphers.caesar.coding(arr_inf_code[:-1], int(arr_inf_code[-1])), parse_mode='Markdown')
        
    if name_code == "caesar_decode":
        if len(arr_inf_code) < 2:
            bot.send_message(message.from_user.id, "error info")
        else:
            bot.send_message(message.from_user.id, ciphers.caesar.decoding(arr_inf_code[:-1], int(arr_inf_code[-1])), parse_mode='Markdown')
    
    if name_code == "vigener_code":        
        if len(arr_inf_code) < 2:
            bot.send_message(message.from_user.id, "error info")
        else:
            bot.send_message(message.from_user.id, ciphers.vigener.coding(' '.join(arr_inf_code[:-1]), arr_inf_code[-1]))

    if name_code == "vigener_decode":        
        if len(arr_inf_code) < 2:
            bot.send_message(message.from_user.id, "error info")
        else:
            bot.send_message(message.from_user.id, ciphers.vigener.decoding(' '.join(arr_inf_code[:-1]), arr_inf_code[-1]))

    if name_code == "qwerty":
            bot.send_message(message.from_user.id, ciphers.qwerty.decoding(' '.join(arr_inf_code)))

    if name_code == "decryption":
        step = ciphers.caesar.decryption(arr_inf_code)
        if step != 0:
            bot.send_message(message.from_user.id, "caesar")
            bot.send_message(message.from_user.id, ciphers.caesar.decoding(arr_inf_code, step))
            bot.send_message(message.from_user.id, "step: " + str(33 - step))
        else:
            bot.send_message(message.from_user.id, "no caesar")
        
        key = ciphers.vigener.decryption(arr_inf_code)
        if key != 0:
            bot.send_message(message.from_user.id, "vigener")
            bot.send_message(message.from_user.id, ciphers.vigener.decoding(' '.join(arr_inf_code), key))
            bot.send_message(message.from_user.id, "key: " + str(key))
        else:
            bot.send_message(message.from_user.id, "no vigener")
        
        if ciphers.qwerty.decryption(inf_code):
            bot.send_message(message.from_user.id, "qwerty")
            bot.send_message(message.from_user.id, ciphers.qwerty.decoding(inf_code))
        else:
            bot.send_message(message.from_user.id, "no qwerty")

    name_code = None

# создание dictionary_ru_words
# additional_functions.download_dictionary_words.download_dictionary()   

name_code = None
bot.polling(none_stop=True, interval=0) 