import gspread
from google.oauth2.service_account import Credentials
# Secret word that the player is trying to guess, taken from list of 345 words
import random
from words import list_of_words

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# SHEET = GSPREAD_CLIENT.open('list_of_words')


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
                """
]
    return stages[guesses_remaining]

guesses = []
guesses_remaining = 6
wrong = 0
# Randomly chooses a word from the list 0f words
word_index = random.randint(0, len(list_of_words)-1)  
word = list_of_words[word_index].lower()
print(word)


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

    guess = input(f"Letters guessed:{guesses}\nYou have {guesses_remaining} guess(es) left, your next guess: ")
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
    print(f"YOU GOT IT!! The word was {word}!")
else:
    print(f"Game over! The word was *{word}*")
#    while input("Want to play again? (Y/N): ") == "Y":
#    print(word)
#    play_game()
