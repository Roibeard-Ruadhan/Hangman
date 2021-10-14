# Secret word that the player is trying to guess, taken from list of 345 words
import random
from words import list_of_words


def hangman_display(guesses_remaining):
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
    f"Welcome to Hangman, before we start please confirm your name: ")

"""
A loop going through each guess until the game reaches it's completion at 0
"""
game_over = False
# def play_game():
while not game_over:
    print(hangman_display(guesses_remaining))
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")
    if guesses == int():
        print('Please use only letters')
    guess = input(
        f"Letters guessed:{guesses}\nYou have {guesses_remaining}" +
        " guess(es) left\nYour next guess is: ")
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
    print(f"Game over {name}! The word was {word}")
"""
game_over = True
Question = input("Would you like to play again Y/N: ")
if Question == ("Y"):
    while not game_over
    print("Lets play {name}")
elif Question == ("N"):
    print("Thank you for playing, have an awesome day!")
"""