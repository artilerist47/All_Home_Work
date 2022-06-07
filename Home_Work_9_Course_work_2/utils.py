import random
import requests
import json
from basic_word import BasicWord


def load_random_word():
    words = []
    try:
        responce = requests.get("https://jsonkeeper.com/b/BRRN")
        words_list = responce.json()
    except:
        with open("words.json", encoding="utf-8") as file:
            words_list = json.load(file)
    for text in words_list:
        random.shuffle(words)
        words.append(BasicWord(text['word'], text['subwords']))

    return words
