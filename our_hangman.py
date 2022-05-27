from ast import AnnAssign
import random
import pyfiglet
import re
import string
from time import sleep
from slowprint.slowprint import *


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# print(BColors.FAIL + "Example text" + BColors.ENDC)

HANGMAN = (
    """
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
    """
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
    """
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
    """
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
    """
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
    """
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
    """
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
    """
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")


def greet_player():
    ascii_banner = pyfiglet.figlet_format("Welcome to Hangman!")
    slowprint(BColors.OKGREEN + ascii_banner + BColors.ENDC, 0.01)
    player_name = input("How can we call you? : ")
    if player_name.upper().lower() == "quit":
        goodbye()
    print("Welcome to Hangman,", player_name + '!')
    return player_name


def goodbye():
    goodbye_anim = pyfiglet.figlet_format("Goodbye!")
    slowprint(BColors.WARNING + goodbye_anim + BColors.ENDC, 0.01)
    exit()


def welcome_back(player_name, is_win):
    print()
    random.seed()
    random_message_index = random.randint(0, 2)
    if is_win == 0:
        if random_message_index == 0:
            print(BColors.OKCYAN + "Welcome back",
                  player_name + "! Let's try again! Try to save the man from cruelty!" + BColors.ENDC)
        elif random_message_index == 1:
            print(BColors.OKCYAN + "If you don't try, you never fail", player_name + "!" + BColors.ENDC)
        elif random_message_index == 2:
            print(BColors.OKCYAN + "There is no failure except in no longer trying! Let's keep going",
                  player_name + "!" + BColors.ENDC)
    elif is_win == 1:
        if random_message_index == 0:
            print(BColors.OKBLUE + "We can see you are good at it",
                  player_name + "! Do you know names of all the countries on earth though?" + BColors.ENDC)
        elif random_message_index == 1:
            print(BColors.OKBLUE + "Winners are not afraid of losing. But losers are. Failure is part of the process "
                                   "of success", player_name + "!" + BColors.ENDC)
        elif random_message_index == 2:
            print(BColors.OKBLUE + "Many innocent people are to be saved",
                  player_name + "! Please be quick!" + BColors.ENDC)


def get_level():
    print("\nWe are going to draw a country or a capital from a long list for you. ")
    print("We have divided the words by a number of distinctive letters into 3 groups.")
    print(" 1 - Easy")
    print(" 2 - Medium")
    print(" 3 - Hard")
    while True:
        try:
            print("Please select level of difficulty: ")
            level = input("")
            if level.upper().lower() == "quit":
                goodbye()
            level = int(level)
        except ValueError:
            print("Please enter a valid character. ")
            continue
        while level > 3 or level <= 0:
            level = input("You have chosen wrong level, please try again. ")
            if level.upper().lower() == "quit":
                goodbye()
            level = int(level)
        break

    if level == 1:
        print("You've chosen easy level. ")
    elif level == 2:
        print("You've chosen medium level. ")
    else:
        print("You've chosen hard level. ")
    return int(level)


def damage(level):
    if level == 1:
        damage_local = 1
    elif level == 2:
        damage_local = 3
    else:
        damage_local = 6
    return damage_local


def create_word_list(filepath="./countries-and-capitals.txt"):
    word_list_local = []
    with open(filepath, newline='') as file:
        for line in file.read().splitlines():
            words_local = line.split("|")
            for word in words_local:
                word_list_local.append(word.strip())
    return word_list_local


def draw_word_from_list(word_list, level):
    random.seed()
    word_number = random.randint(0, len(word_list) - 1)
    word = word_list[word_number]

    if level == 1:
        while len(word) > 5:
            word_number = random.randint(0, len(word_list) - 1)
            word = word_list[word_number]
        return word

    elif level == 2:
        while len(word) <= 5 or len(word) > 8:
            word_number = random.randint(0, len(word_list) - 1)
            word = word_list[word_number]
        return word

    else:
        while len(word) <= 8:
            word_number = random.randint(0, len(word_list) - 1)
            word = word_list[word_number]
        return word


def guess_letter(word, encoded_word, level, wrong_guesses, guess_counter, already_guessed):
    az_check = string.ascii_letters
    is_tried = 0
    guess = input("Please enter your guess: ")
    if guess.upper().lower() == "quit":
        goodbye()
    while len(guess) > 1:
        guess = input("Please enter only one character. ")
        if guess.upper().lower() == "quit":
            goodbye()
    while guess not in az_check:
        guess = input("Please use A-Z characters.")
        if guess.upper().lower() == "quit":
            goodbye()
    for letter in range(0, len(word)):
        if word[letter] == guess.upper() or word[letter] == guess.lower():
            if word[letter].isupper():
                guess = guess.upper()
            elif word[letter].islower():
                guess = guess.lower()
            encoded_word = encoded_word[0:letter] + guess + encoded_word[letter + 1:len(word)]
            guess_counter += 1
    if guess_counter == 0 and guess.upper() not in already_guessed:
        already_guessed.append(guess.upper())
        wrong_guesses = wrong_guesses + damage(level)
    elif guess.upper() in already_guessed:
        is_tried = 1


    return wrong_guesses, encoded_word, already_guessed, is_tried


def get_hangman(max_wrong_guesses, graphics_list):
    return int(max_wrong_guesses / (len(graphics_list) - 1))


def input_check_play_again(decision_local=""):
    """input_check_play_again() takes a string (player input) and checks if it is of the expected format.
    If the string meets the requirements, it is returned.
    Otherwise the user is asked repetitively to provide a proper input and runs it against
    the checks until the input meets the requirements and only then is returned.

    In: str, default = ''
    Out: str decision that  is either 'Y', 'y', 'N', 'n'"""
    while decision_local.lower() != "y" and decision_local != "n":
        decision_local = input("I didn't get it! Would you like to play? Yes or no? (y/n) ")
        if decision_local.upper().lower() == "quit":
            goodbye()
    return decision_local.lower()


def main(game_round, player_name=""):
    if game_round == 'first':
        player_name = greet_player()
    elif game_round == 'next':
        welcome_back(player_name, 1)
    elif game_round == 'fail':
        welcome_back(player_name, 0)
    level = get_level()
    word_base = create_word_list()
    word_to_guess = draw_word_from_list(word_base, level)
    original_word = word_to_guess
    encoded_word = re.sub('[0-9a-zA-Z]', '_', word_to_guess)
    # print(word_to_guess)  # Print selected word
    print(HANGMAN[0])  # Starting Hangman
    print(encoded_word)  # Print word with _
    already_guessed = []
    max_wrong_guesses = 42  # Must be every 3
    wrong_guesses = 0  # Starting value
    guess_counter = 0  # Starting value for loop

    # =================================== MAIN GAME LOGIC ============================================
    while wrong_guesses < max_wrong_guesses and "_" in encoded_word:
        game_state_tuple = guess_letter(word_to_guess, encoded_word, level, wrong_guesses, guess_counter,
                                        already_guessed)
        wrong_guesses = game_state_tuple[0]
        encoded_word = game_state_tuple[1]
        already_guessed = game_state_tuple[2]
        is_tried_message = game_state_tuple[3]
        hangman_graphics_index = int(wrong_guesses / get_hangman(max_wrong_guesses, HANGMAN))
        print(HANGMAN[hangman_graphics_index])

        print("Letters you've guessed wrong:")
        for i in already_guessed:
            print(BColors.WARNING + i, " " + BColors.ENDC, end="")
        print(" ")
        # Print encoded word
        print(BColors.BOLD + encoded_word + BColors.ENDC, BColors.FAIL + "\tyour damage: ", str(wrong_guesses) + "/" +
              str(max_wrong_guesses) + BColors.ENDC)
        if is_tried_message:
            print(BColors.OKCYAN + "You've already provided that character. " + BColors.ENDC)
    if wrong_guesses == max_wrong_guesses:
        decision = input("So sorry, you've failed! The word was %s. Do you want to play again? (y/n) " % original_word)
        if decision.upper().lower() == "quit":
            goodbye()
        decision = input_check_play_again(decision)
        try:
            if decision.lower() == "y":
                main("fail", player_name)
            elif decision.lower() == 'n':
                print("I hope you enjoyed the game! See you next time!")
            else:
                raise ValueError
        except ValueError:
            input_check_play_again()
    else:
        decision = input("Congratulations, you've won the game! Do you want to try again? (y/n) ")
        if decision.upper().lower() == "quit":
            goodbye()
        decision = input_check_play_again(decision)
        try:
            if decision.lower() == "y":
                main("next", player_name)
            elif decision.lower() == 'n':
                print("Thank you for your time. See you in the next one!")
            else:
                raise ValueError
        except ValueError:
            input_check_play_again()


if __name__ == '__main__':
    main("first")
