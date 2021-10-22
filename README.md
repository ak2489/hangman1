![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)
# HANGMAN
Hangman is a Python terminal game, which runs in the Code Institue mock terminal on Heroku.

Users try to guess the letters of the hidden word before they run out of lives. Each wrong guess takes away 1 life. 

[Here is the live version of my project.](https://hangman-ak.herokuapp.com/)


![responsive](assets/docs/responsive.jpg)

## User Experience

### User Stories
#### First Time Visitor Goals
a. As a first time visitor, I want to be able to start the game easily.

b. As a first time visitor, I want to be challenged by the game.

c. As a first time visitor, I want to be able to run the game again easily so i can keep playing.

#### Returning Visitor Goals
a. As a returning visitor, I want to continue to be challenged with a choice of dificulty level. 

b. As a returning visitor, I want to keep track of my score.

c. As a returning visitor, I want to be able to challenege other users. 

## Design 
![Wireframe](assets/docs/hangman_wireframe.jpg)
* Command line game that has the hangman frame above the word that is hidden by '_'.

## How To Play

Hangman is a paper and pencil guessing game for two or more players. One player thinks of a word, phrase or sentence and the other(s) tries to guess it by suggesting letters within a certain number of guesses. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game))

In this version the player enters their name and then a random word is generated for the player to guess.

The player can see how many lives they have and are asked to guess a letter. After guessing a letter the letter will either appear in the word or take away a life in which case the frame of the hangman will be drawn. All letters guessed are shown below the lives. 

The player then keeps guessing until they either get the word or run out if lives.If the player gets the word you get a message of Congratulations. If the player does not get the word in the amount of lives the word will be revealed. Afer etiher event the player will be asked to play again which well then randomly generate a new word to play.

## Features

