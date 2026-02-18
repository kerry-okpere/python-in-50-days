# Hang man
# if user guesses correct and the word still has letters not guessed, repeat asking the user for the next letter
# if the user guess all letters correctly, they win
# if the user guess a letter incorrectly, add a new part to the hangman picture
# if the hangman picture if fully drawn, the user lose

import random
from hang_man import HANGMANPICS, word_list

failed_attempts = 0


def hangman_game():
    global failed_attempts
    # guess word
    random_word = random.choice(word_list)
    guessing_letters = ["_"] * len(random_word)
    ##########

    attempt_limit = len(HANGMANPICS) - 1

    while "_" in guessing_letters and attempt_limit > failed_attempts:
        letter_guessed = input(
            f"Guess a letter in the word: {''.join(guessing_letters)}\n"
        ).lower()

        if letter_guessed in random_word:
            index_of_letter = random_word.index(letter_guessed)
            guessing_letters[index_of_letter] = letter_guessed
            print(f"Correct! {''.join(guessing_letters)}")
        else:
            failed_attempts += 1
            print(
                f"{HANGMANPICS[failed_attempts]} \nWrong guess! You have {attempt_limit - failed_attempts} attempts left."
            )

    if "_" not in guessing_letters:
        print(f"Congratulations! You guessed the word {random_word} correctly!")
    else:
        print(f"Game over! The word was {random_word}.")


print("Welcome to Hangman!")
hangman_game()
