import random
import string
from words import words
from hangman_visual import lives_visual_dict


def start():
    """Sets the game up for the user asking for name
    and if they would like to start"""
    print(
        """
         _   _
        | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __
        | |_| |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
        |  _  | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                            |___/
        """
    )
    name = input('What is your name?\n')
    print('Hello, ' + name)
    if input('Would you like to play Hangman? (Y/N)').upper() == "Y":
        hangman()

    elif input().upper() == "N":
        print('Goodbye!')

    else:
        print('Invaild entry please select Y or N.')
        start()


# function to get random word from list
def get_word():
    """Picks a random word from words.py that the player has to guess"""
    word = random.choice(words)  # randomly chooses something from the list

    return word.upper()


# function for game
def hangman():
    """Play the game"""
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
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter:\n').upper()
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
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
        restart_game()
    else:
        print('You have guessed the word', word, '\nCongratulations!!')
        restart_game()


def restart_game():
    """ Gives player option to restart, otherwise returns to title screen """
    game_restart = False

    while not game_restart:
        restart = input('Would you like to play Hangman? (Y/N)\n').upper()

        if restart == "Y":
            game_restart = True
            hangman()

        elif restart == "N":
            game_restart = True
            print('Goodbye!')
            start()

        else:
            print('You must select Y or N. Please try again.')


if __name__ == "__main__":
    start()
