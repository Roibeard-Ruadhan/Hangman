# Secret word that the player is trying to guess, taken from list of 300+ words
import random
from words import list_of_words

# Hangman image code sourced from google


def hangman_display(guesses_remaining):
    """
    Images of the hangman to be released at certain stages to show at what
    stage the hangman game is at visually
    """
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial state before wrong guesses
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """]
    return stages[guesses_remaining]


guesses = []
guesses_remaining = 6
wrong = 0
"""
Randomly chooses a word from the list 0f words
"""
word_index = random.randint(0, len(list_of_words)-1)
word = list_of_words[word_index].lower()
print(word)
name = input(
    "Welcome to Hangman, before we start please confirm your name: ")

"""
A loop going through each guess until the game reaches it's completion at 0.
Within this loop I have set all the criteria to be completed before the game
can end
"""

game_over = False
allowed_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# def play_game():
while not game_over:
    print(hangman_display(guesses_remaining))
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")
    guess = ""
    if len(guess) == 1:
        guess = input(
            f"Letters guessed:{guesses}\nYou have {guesses_remaining}" +
            " guess(es) left\n\nPlease enter your guess(letter) here: ")
    # Below is an attempt to block user from using more than one letter
    else:
        len(guess) != 1
        guess = input(
            f"Please guess only 1 *Letter*.\n Letters guessed:{guesses}\nYou have {guesses_remaining}" +
            " guess(es) left\nPlease enter your guess(letter) here: ")
        if any(x not in allowed_characters for x in guess):
            print(guess, "= *invalid character/not a letter*")
        else:
            print(guess, 'is valid\n')
            guesses.append(guess.lower())
            if guess.lower() not in word.lower():
                guesses_remaining -= 1
                if guesses_remaining == 0:
                    break

            game_over = True
            for letter in word:
                if letter.lower() not in guesses:
                    game_over = False

if game_over:
    print(f"You got it {name} \u2665!! The word was {word} \u2665!! ")
else:
    print("""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """)
    print(f"Game over {name}! The word was {word}")

