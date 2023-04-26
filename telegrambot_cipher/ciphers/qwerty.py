# -*- coding: cp1251 -*-

import pymorphy2
import additional_functions.download_dictionary_words
from itertools import cycle, product


arr_words_ru = additional_functions.download_dictionary_words.get_hashed_arr_words('russian.txt')
arr_words_eng = additional_functions.download_dictionary_words.get_hashed_arr_words('english.txt')
arr_words = arr_words_ru + arr_words_eng

alph_eng = [chr(i) for i in range(ord('a'), ord('z')+1)]
alph_ru = [chr(i) for i in range(ord('а'), ord('я')+1)]
alph_ru = alph_ru[:6] + ['ё'] + alph_ru[6:]
dict_alph = {'ru': alph_ru, 'eng': alph_eng}
str_keyboard_ru = "ёйцукенгшщзхъфывапролджэячсмитьбю."
str_keyboard_eng = "`qwertyuiop[]asdfghjkl;'zxcvbnm,./"
ditc_keyboard_layout = {'ru': str_keyboard_ru, 'eng': str_keyboard_eng}


def decoding(text):
    if any(simvol in alph_eng for simvol in text):
        alph = 'eng'
        reverse_alph = "ru"
    else:
        alph = 'ru'
        reverse_alph = "eng"
    text_for_encode = ''
    for i in range(len(text)):
        if text[i] in ditc_keyboard_layout[alph]:
            ind_simv_in_str = ditc_keyboard_layout[alph].index(text[i:i+1]) # с символами не работает 
            text_for_encode += ditc_keyboard_layout[reverse_alph][ind_simv_in_str:ind_simv_in_str+1]
        else:
            text_for_encode += text[i]
    
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
    """
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
"""
    if any(simvol in alph_eng for simvol in text):
        reverse_alph = 'ru'    
        alph = 'eng'
    else:
        reverse_alph = 'eng'
        alph = 'ru'
    decoded_text = decoding(text)
    if any(exist_word(word) for word in decoded_text.split()):
        return True
    return False

def exist_word(word):
    if hash(word+"\n") in arr_words:
        return True
    else:
        return False

if __name__ == "__main__": 
    code()