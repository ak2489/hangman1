import random
from words import words


# function to get random word from list
def get_word():
    word = random.choice(words)  # randomly chooses something from the list

    return word.upper()


print(get_word())
