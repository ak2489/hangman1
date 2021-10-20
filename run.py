import random
import string
from words import words


# function to get random word from list
def get_word():
    """function to get random word from list"""
    word = random.choice(words)  # randomly chooses something from the list

    return word.upper()


# function for game
def hangman():
    """function for hangman game"""
    word = get_word()
    word_letters = set(word)  # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    # getting user input
    while len(word_letters) > 0:
        # letters used
        print('You have used there letters: ', ' '.join(used_letters))
    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print('You have already used that character. Please try again.')

    else:
        print('Invalid character. Please try again.')

    # gets here when len(word_letters) == 0

hangman()