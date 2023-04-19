# -*- coding: cp1251 -*-

import pymorphy2
import additional_functions.download_dictionary_ru_words


arr_words = additional_functions.download_dictionary_ru_words.get_hashed_arr_words('russian.txt')

alph_eng = [chr(i) for i in range(ord('a'), ord('z')+1)]
alph_ru = [chr(i) for i in range(ord('а'), ord('я')+1)]
alph_ru = alph_ru[:6] + ['ё'] + alph_ru[6:]
dict_alph = {'ru': alph_ru, 'eng': alph_eng}


def decoding_word(word, step):
    s = ''
    word_for_encode = ''
    for i in range(len(word)):
        if word[i] in dict_alph['ru']:
            word_for_encode += word[i]
    for w in word_for_encode: 
        ind = alph_ru.index(w)
        if ind + int(step%33) >= 33:            
            s += alph_ru[int(step%33)-(33-ind)]
        else:
            s += alph_ru[ind + int(step%33)]
    # добавление пробелов в расшифрованное сообщение
    for i in range(len(word)):
        if word[i:i+1] not in dict_alph['ru']:
            s = s[:i] + word[i:i+1] + s[i:]
    return s

def coding_word(word, step):
    s = ''
    word_for_encode = ''
    for i in range(len(word)):
        if word[i] in dict_alph['ru']:
            word_for_encode += word[i]
    for w in word_for_encode: 
        ind = alph_ru.index(w)
        if ind + int(step%33) >= 33:            
            s += alph_ru[int(step%33)-(33-ind)]
        else:
            s += alph_ru[ind + int(step%33)]
    # добавление пробелов в расшифрованное сообщение
    for i in range(len(word)):
        if word[i:i+1] not in dict_alph['ru']:
            s = s[:i] + word[i:i+1] + s[i:]
    return s

def coding(arr_encoded_words, step):
    arr_decoded = []
    for encoded_word in arr_encoded_words:
        arr_decoded.append(coding_word(encoded_word, step))
    return ' '.join(arr_decoded)

def decoding(arr_encoded_words, step):
    arr_decoded = []
    for encoded_word in arr_encoded_words:
        arr_decoded.append(coding_word(encoded_word, step))
    return ' '.join(arr_decoded)

def code(text, step = 1):
    return coding(text, step)

def decryption_word(word):                       #дешифровка сообщения
    arr_step = []
    for step in range(1, 34):
        encoded_word = decoding_word(word, step)
        if exist_word(encoded_word):
            arr_step.append(step)
    return arr_step

def decryption(arr_encoded_words):
    arr_steps = []
    count_words = len(arr_encoded_words)
    if count_words > 3:
        count_checked_words = 3
    else:
        count_checked_words = count_words

    for i in range(count_checked_words):
        arr_steps.append(decryption_word(arr_encoded_words[i]))
    """
    arr = []
    for i in arr_steps[0]:
        if i in arr_steps[1]:
            arr.append(i)
    arr2 = []
    if len(arr_steps) > 2:
        for i in arr:
            if i in arr_steps[2]:
                arr2.append(i)
        if arr2 != []:
            return arr2[0]
    else:
        if arr != []:
            return arr[0]
    """
    arr_probable_decryption = arr_steps[0]
    if count_checked_words > 1:
        for i in range(count_checked_words-1):
            if arr_steps[i] == []:
                return 0
            arr_probable_decryption = list(set(arr_probable_decryption)&set(arr_steps[i+1]))
    if arr_probable_decryption == []:
        return 0
    return arr_probable_decryption[0]

def exist_word(word):
    h = hash(word+'\n')
    if h in arr_words:
        return True
    else:
        return False

if __name__ == "__main__": 
    code()