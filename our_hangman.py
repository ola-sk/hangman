from ast import AnnAssign
import random
import pyfiglet
import re
import string


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
    print(BColors.OKGREEN + ascii_banner + BColors.ENDC)
    player_name = input("How can we call you? : ")
    print("Welcome to Hangman,", player_name + '!')
    return player_name


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
            level = int(input(""))
        except ValueError:
            print("Please enter a valid character. ")
            continue
        while level > 3 or level <= 0:
            level = int(input("You have chosen wrong level, please try again. "))
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
    guess = input("Please enter your guess: ")
    while len(guess) > 1:
        guess = input("Please enter only one character. ")
    while guess not in az_check:
        guess = input("Please use A-Z characters.")
    for letter in range(0, len(word)):
        if word[letter] == guess.upper() or word[letter] == guess.lower():
            if (word[letter].isupper()):
                guess = guess.upper()
            elif (word[letter].islower()):
                guess = guess.lower()
            encoded_word = encoded_word[0:letter] + guess + encoded_word[letter + 1:len(word)]
            guess_counter += 1
    if guess_counter == 0 and guess not in already_guessed:
        already_guessed.append(guess.upper())
        wrong_guesses = wrong_guesses + damage(level)

    return wrong_guesses, encoded_word, already_guessed


def get_hangman(max_wrong_guesses, graphics_list):
    return int(max_wrong_guesses / (len(graphics_list) - 1))


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
    while wrong_guesses < max_wrong_guesses and "_" in encoded_word:
        hidden_letters = guess_letter(word_to_guess, encoded_word, level, wrong_guesses, guess_counter, already_guessed)
        wrong_guesses = hidden_letters[0]
        encoded_word = hidden_letters[1]
        already_guessed = hidden_letters[2]
        hangman_graphics_index = int(wrong_guesses / get_hangman(max_wrong_guesses, HANGMAN))
        print(HANGMAN[hangman_graphics_index])
        print(already_guessed)  # Print already guessed
        print(hidden_letters[1], hidden_letters[0])  # Print encoded word
    if wrong_guesses == max_wrong_guesses:
        decision = input("So sorry, you've failed! The word was %s Do you want to play again? (y/n) "% original_word)
        if decision == "y":
            main("fail", player_name)
    else:
        decision = input("Congratulations, you've won the game! Do you want to try again? (y/n) ")
        if decision == "y":
            main("next", player_name)


if __name__ == '__main__':
    main("first")

# TODO: rozważ przypadek, gdzie wpiszemy spację jako zgadywaną literę. Obecnie wlicza spację, chcemy nie wliczać
