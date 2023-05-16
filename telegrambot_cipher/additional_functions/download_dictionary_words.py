import requests

def sorted_dictionary(path):
    file_ru_words = open(path, "r", encoding="utf_8")
    words_arr = sorted(list(file_ru_words.readlines()))
    file_ru_words.close()
    file_ru_words = open(path, "w", encoding="utf_8")
    for i in range(len(words_arr)):
        file_ru_words.write(words_arr[i])
    file_ru_words.close()


def download_dictionary():
    response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt')
    text = response.content.decode('cp1251')
    with open('russian.txt', 'wb') as ru:
        ru.write(text.encode('utf-8'))
    sorted_dictionary('russian.txt')
    """
    response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian_surnames.txt')
    text = response.content.decode('cp1251')
    with open('russian_surnames.txt', 'wb') as ru:
        ru.write(text.encode('utf-8'))
    """

def get_arr_words(path): 
    file_ru_words = open(path, "r", encoding="utf_8")
    words_arr = sorted(list(file_ru_words.readlines()))
    file_ru_words.close()
    return words_arr

def get_hashed_arr_words(path):
    file_ru_words = open(path, "r", encoding="utf_8")
    words_arr = []
    line = file_ru_words.readline()
    while line != '':
        words_arr.append(hash(line))
        line = file_ru_words.readline()
    file_ru_words.close()
    return words_arr

if __name__ == "__main__": 
    download_dictionary()
