# -*- coding: cp1251 -*-

import additional_functions.download_dictionary_words


arr_words_ru = additional_functions.download_dictionary_words.get_hashed_arr_words('russian.txt')
arr_words_eng = additional_functions.download_dictionary_words.get_hashed_arr_words('english.txt')
arr_words = arr_words_ru + arr_words_eng

alph_eng = [chr(i) for i in range(ord('a'), ord('z')+1)]
alph_ru = [chr(i) for i in range(ord('а'), ord('я')+1)]
alph_ru = alph_ru[:6] + ['ё'] + alph_ru[6:]
dict_alph = {'ru': alph_ru, 'eng': alph_eng}


def coding_word(word, step):
    s = ''
    if any(simvol in alph_eng for simvol in word):
        alph = dict_alph['eng']
        n = 23
    if any(simvol in alph_ru for simvol in word):
        alph = dict_alph['ru']
        n = 33
    word_for_encode = ''
    for i in range(len(word)):
        if word[i] in alph:
            word_for_encode += word[i]
    for w in word_for_encode: 
        ind = alph.index(w)
        if ind + int(step%n) >= n:            
            s += alph[int(step%n)-(n-ind)-1]
        else:
            s += alph[ind + int(step%n)]

    # добавление символов в расшифрованное сообщение
    for i in range(len(word)):
        if word[i:i+1] not in alph:
            s = s[:i] + word[i:i+1] + s[i:]
    return s

def coding(arr_encoded_words, step):
    arr_decoded = []
    for encoded_word in arr_encoded_words:
        arr_decoded.append(coding_word(encoded_word, step))
    return ' '.join(arr_decoded)

def decoding_word(word, step):
    s = ''
    if any(simvol in alph_eng for simvol in word):
        alph = dict_alph['eng']
        n = 23
    if any(simvol in alph_ru for simvol in word):
        alph = dict_alph['ru']
        n = 33
    word_for_encode = ''
    for i in range(len(word)):
        if word[i] in alph:
            word_for_encode += word[i]
    for w in word_for_encode: 
        ind = alph.index(w)
        if ind - int(step%n) < 0:            
            s += alph[n - (int(step%n) - ind)]
        else:
            s += alph[ind - int(step%n)]

    # добавление символов в расшифрованное сообщение
    for i in range(len(word)):
        if word[i:i+1] not in alph:
            s = s[:i] + word[i:i+1] + s[i:]
    return s

def decoding(arr_encoded_words, step):
    arr_decoded = []
    for encoded_word in arr_encoded_words:
        arr_decoded.append(decoding_word(encoded_word, step))
    return ' '.join(arr_decoded)

def decryption_word(word):
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
