# -*- coding: cp1251 -*-

import pymorphy2
import additional_functions.download_dictionary_ru_words
from itertools import cycle, product


arr_words = additional_functions.download_dictionary_ru_words.get_hashed_arr_words('russian.txt')


alph_eng = [chr(i) for i in range(ord('a'), ord('z')+1)]
alph_ru = [chr(i) for i in range(ord('а'), ord('я')+1)]
alph_ru = alph_ru[:6] + ['ё'] + alph_ru[6:]
dict_alph = {'ru': alph_ru, 'eng': alph_eng}
str_keyboard_ru = "ёйцукенгшщзхъфывапролджэячсмитьбю."
str_keyboard_eng = "`qwertyuiop[]asdfghjkl;'zxcvbnm,./"
ditc_keyboard_layout = {'ru': str_keyboard_ru, 'eng': str_keyboard_eng}


def adding_characters(text, shifre):
    # добавление пробелов в расшифрованное сообщение
    for i in range(len(text)):
        if text[i:i+1] == ' ':
            shifre = shifre[:i] + text[i:i+1] + shifre[i:]
    return shifre

def decoding(text, key):
    if any(simvol in alph_eng for simvol in text):
        alph = 'eng'
    elif any(simvol in alph_ru for simvol in text):
        alph = 'ru'
    
    if shifre_decode == '':
        return "empty"
    return adding_characters(text, shifre_decode)

def coding(text, key):
    if any(simvol in alph_eng for simvol in text):
        alph = 'eng'
    if any(simvol in alph_ru for simvol in text):
        alph = 'ru'
    
    if shifre_decode == '':
        return "empty"
    return adding_characters(text, shifre_decode)

def code(text, key):
    return coding(text, key)

def decryption_word(word):   
    if any(simvol in alph_eng for simvol in word):
        reverse_alph = 'ru'    
        alph = 'eng'
    if any(simvol in alph_ru for simvol in word):
        reverse_alph = 'eng'
        alph = 'ru'
    revers_word = ''
    for i in range(len(word)):
        ind_simv_in_str = ditc_keyboard_layout[alph].index(word[i:i+1]) # с символами не работает 
        revers_word += ditc_keyboard_layout[reverse_alph][ind_simv_in_str:ind_simv_in_str+1]
    if exist_word(revers_word):
        return True
    return False


def decryption(arr_encoded_words):
    if any(simvol in str_keyboard_eng for simvol in arr_encoded_words[0]):
        reverse_alph = 'ru'
        alph = 'eng'
    if any(simvol in str_keyboard_ru for simvol in arr_encoded_words[0]):
        reverse_alph = 'eng'
        alph = 'ru'
    text = " ".join(arr_encoded_words)
    if not any(decryption_word(arr_encoded_words[i]) for i in range(len(arr_encoded_words))):
        return 0
    revers_encoded_words = ''
    for i_word in range(len(arr_encoded_words)):
        for i_sim in range(len(arr_encoded_words[i_word])):
            ind_simv_in_str = ditc_keyboard_layout[alph].index(arr_encoded_words[i_word][i_sim:i_sim+1])
            revers_encoded_words += ditc_keyboard_layout[reverse_alph][ind_simv_in_str:ind_simv_in_str+1]
    revers_encoded_words = adding_characters(text, revers_encoded_words)
    return ''.join(revers_encoded_words)

def exist_word(word):
    if hash(word+"\n") in arr_words:
        return True
    else:
        return False

if __name__ == "__main__": 
    code()