import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# SHEET = GSPREAD_CLIENT.open('list_of_words')

import random
from words import list_of_words

def hangman_display(guesses):
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
    return stages[guesses]

guesses = []
guesses_remaining = 6
wrong = 0
word_index = random.randint(0, len(list_of_words)-1)
word = list_of_words[word_index].upper()
print(word)
print(hangman_display(guesses_remaining))


game_over = False

while not game_over:
   for letter in word:
      if letter.lower() in guesses:
         print(letter, end=" ")
      else:
         print("_", end=" ")
   print("") 

   guess = input(f"You have {guesses_remainin, your next Guess: ")
   guesses.append(guess.upper())
   if guess.lower() not in word.upper():
      guesses_remaining -= 1:
      if allowed_errors == 0:
         break
game_over = True

