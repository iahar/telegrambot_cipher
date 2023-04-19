# -*- coding: cp1251 -*-

import pymorphy2
import additional_functions.download_dictionary_ru_words
from itertools import cycle, product


arr_words = additional_functions.download_dictionary_ru_words.get_hashed_arr_words('russian.txt')


alph_eng = [chr(i) for i in range(ord('a'), ord('z')+1)]
alph_ru = [chr(i) for i in range(ord('а'), ord('я')+1)]
alph_ru = alph_ru[:6] + ['ё'] + alph_ru[6:]
dict_alph = {'ru': alph_ru, 'eng': alph_eng}



def form_dict(alph):
    return dict([(i, dict_alph[alph][i]) for i in range(len(dict_alph[alph]))])

def comparator(value, key):
    return dict([(idx, [ch[0], ch[1]]) for idx, ch in enumerate(zip(value, cycle(key)))])

def encode_val(word):
    if word[0] in alph_eng:
        d = form_dict('eng')
    if word[0] in alph_ru:
        d = form_dict('ru')
    return [k for c in word for k,v in d.items() if v == c]

def full_encode(value, key, alph):
    d = comparator(value, key)
    l = len(form_dict(alph))
    return [(v[0] + v[1]) % l for v in d.values()]

def decode_val(list_in, alph):
    l = len(list_in)
    d = form_dict(alph)
    return [d[i] for i in list_in if i in d]

def full_decode(value, key, alph):
    d = comparator(value, key)
    l = len(form_dict(alph))
    return [(v[0] - v[1]) % l for v in d.values()]


def adding_characters(text, shifre):
    # добавление символов в расшифрованное сообщение
    for i in range(len(text)):
        if text[i:i+1] not in alph_ru+alph_eng:
            shifre = shifre[:i] + text[i:i+1] + shifre[i:]
    return shifre

def decoding(text, key):
    if any(simvol in alph_eng for simvol in text):
        alph = 'eng'
    elif any(simvol in alph_ru for simvol in text):
        alph = 'ru'
    print(key)
    text_for_encode = ''
    for i in range(len(text)):
        if text[i] in dict_alph[alph]:
            text_for_encode += text[i]
    key_encoded = encode_val(key)
    value_encoded = encode_val(text_for_encode)
    shifre = full_decode(value_encoded, key_encoded, alph)
    shifre_decode = ''.join(decode_val(shifre, alph))
    if shifre_decode == '':
        return "empty"
    return adding_characters(text, shifre_decode)

def coding(text, key):
    if any(simvol in alph_eng for simvol in text):
        alph = 'eng'
    if any(simvol in alph_ru for simvol in text):
        alph = 'ru'
    text_for_encode = ''
    for i in range(len(text)):
        if text[i] in dict_alph[alph]:
            text_for_encode += text[i]
    key_encoded = encode_val(key)
    value_encoded = encode_val(text_for_encode)
    shifre = full_encode(value_encoded, key_encoded, alph)
    shifre_decode = ''.join(decode_val(shifre, alph))
    if shifre_decode == '':
        return "empty"
    return adding_characters(text, shifre_decode)

def code(text, key):
    return coding(text, key)

def decryption_word(word):   
    max_len_key = 2      # все ключи при максимальной длине 3 пробегает за 18 минут, при сравнивании слова с обычным нехэшированным списком
    if any(simvol in alph_eng for simvol in word):
        alph = 'eng'
    if any(simvol in alph_ru for simvol in word):
        alph = 'ru'
    arr_keys = []
    for len_key in range(1, max_len_key+1):
        for key in list(product(dict_alph[alph], repeat=len_key)):
            if exist_word(decoding(word, key)):
                arr_keys.append(key)
    return arr_keys

def decryption(arr_encoded_words):
    if any(simvol in alph_eng for simvol in arr_encoded_words[0]):
        alph = 'eng'
    if any(simvol in alph_ru for simvol in arr_encoded_words[0]):
        alph = 'ru'

    text = ' '. join(arr_encoded_words)
    text_for_encode_with_space = ''
    for i in range(len(text)):
        if text[i] in dict_alph[alph]+[' ']:
            text_for_encode_with_space += text[i]
    arr_encoded_words = text_for_encode_with_space.split()

    count_words = len(arr_encoded_words)
    arr_probable_keys = decryption_word(arr_encoded_words[0])
    if arr_probable_keys == []:
        return 0
    if count_words == 1:       
        return arr_probable_keys[0]
    
    for key in arr_probable_keys:
        if exist_word(decoding(arr_encoded_words[1], key[::-1])):
            if count_words > 2:
                if exist_word(decoding(arr_encoded_words[2], key[::-1])):
                    return ''.join(key)
            else:
                return ''.join(key)
    return ''.join(arr_probable_keys[0])

def exist_word(word):
    if hash(word+"\n") in arr_words:
        return True
    else:
        return False

if __name__ == "__main__": 
    code()