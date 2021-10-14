import random
from words import words

def get_word(words):
    word = random.choice(words)  # randomly chooses something from the list

    return word.upper()

print(get_word(words))
