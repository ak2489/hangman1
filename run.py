import random
from words import words
import string


# function to get random word from list
def get_word():
    word = random.choice(words)  # randomly chooses something from the list

    return word.upper()


# function for game
def hangman():
    word = get_word()
    word_letters = set(word)  # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
