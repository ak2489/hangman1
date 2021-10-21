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

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have', lives, 'lives left')
        print('You have used these letters: ', ' '.join(used_letters))

        # what the current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1  # takes away a life if wrong
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again.')

    # gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You have guessed the word', word, '\n Congratulations!!')


def restart():
    """ Function to restart game after completion"""
    word = get_word()
    hangman()
    while input('Play again? (Y/N)').upper() == "Y":
        word = get_word()
        hangman()


if __name__ == "__main__":
    restart()
