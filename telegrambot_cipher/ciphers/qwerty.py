# -*- coding: cp1251 -*-

import additional_functions.download_dictionary_words
from itertools import cycle, product


arr_words_ru = additional_functions.download_dictionary_words.get_hashed_arr_words('russian.txt')
arr_words_eng = additional_functions.download_dictionary_words.get_hashed_arr_words('english.txt')
arr_words = arr_words_ru + arr_words_eng

alph_eng = [chr(i) for i in range(ord('a'), ord('z')+1)]
alph_ru = [chr(i) for i in range(ord('а'), ord('я')+1)]
alph_ru = alph_ru[:6] + ['ё'] + alph_ru[6:]
dict_alph = {'ru': alph_ru, 'eng': alph_eng}
str_keyboard_ru =  "ёйцукенгшщзхъфывапролджэячсмитьбю."
str_keyboard_eng = "`qwertyuiop[]asdfghjkl;'zxcvbnm,./"
ditc_keyboard_layout = {'ru': str_keyboard_ru, 'eng': str_keyboard_eng}


def decoding(text):
    if text[0:1] in alph_eng and text[1:2] in alph_eng:
        alph = 'eng'
        reverse_alph = "ru"
    else:
        alph = 'ru'
        reverse_alph = "eng"
    text_for_encode = ''
    for i in range(len(text)):
        if text[i:i+1] in ditc_keyboard_layout[alph]:
            ind_simv_in_str = ditc_keyboard_layout[alph].index(text[i:i+1])
            text_for_encode += ditc_keyboard_layout[reverse_alph][ind_simv_in_str:ind_simv_in_str+1]
        else:
            text_for_encode += text[i:i+1]
    if text_for_encode == '':
        return "empty"
    return text_for_encode


def decryption_word(text):   
    if any(simvol in alph_eng for simvol in text):
        reverse_alph = 'ru'    
        alph = 'eng'
    if any(simvol in alph_ru for simvol in text):
        reverse_alph = 'eng'
        alph = 'ru'
    decoded_text = decoding(text)
    if any(exist_word(word) for word in decoded_text.split()):
        return True
    return False


def decryption(text):
    if any(simvol in alph_eng for simvol in text):
        reverse_alph = 'ru'    
        alph = 'eng'
    else:
        reverse_alph = 'eng'
        alph = 'ru'
    decoded_text = decoding(text)
    number_meaningful_words = 0
    for i in range(len(decoded_text.split())):
        word = decoded_text.split()[i]
        if exist_word(word):
            number_meaningful_words += 1
        if i > 5:
            break
    if number_meaningful_words >= 1:
        return True
    return False

def exist_word(word):
    if hash(word+"\n") in arr_words:
        return True
    else:
        return False

if __name__ == "__main__": 
    code()