from ast import AnnAssign
import random
import pyfiglet
import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#print(bcolors.FAIL + "Example text" + bcolors.ENDC)

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


with open("words.txt") as f:
    words = f.read().splitlines()

def get_name():
    player_name = input("Please enter your name. ")
    return player_name

def get_level():  
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

def get_word(words, level):

    word_number = random.randint(0, len(words) -1)
    word = words[word_number].upper()

    if level == 1:
        while len(word) > 5:
            word_number = random.randint(0, len(words) -1)
            word = words[word_number].upper()
        return word

    elif level == 2:
        while len(word) <= 5 or len(word) > 8:
            word_number = random.randint(0, len(words) -1)
            word = words[word_number].upper()
        return word 

    else:
        while len(word) <= 8:
            word_number = random.randint(0, len(words) -1)
            word = words[word_number].upper()
        return word

def damage(level):
    if level == 1:
        damage = 1
    elif level == 2:
        damage = 2
    else:
        damage = 3
    return damage

def get_hangman(max_wrong_guesses):
    return int(max_wrong_guesses / (len(HANGMAN)-1 ))

def guess_letter(word, encoded_word, level, wrong_guesses, guess_counter):
    guess = input("Please enter your guess: ")
    while len(guess) > 1:
        guess = input("Please enter only one character. ")

    for letter in range(0, len(word)):
        if word[letter] == guess.upper():
            encoded_word = encoded_word[0:letter] + guess.upper() + encoded_word[letter+1:len(word)]
            guess_counter += 1
    if guess_counter == 0:
        wrong_guesses = wrong_guesses + damage(level)
        
    return wrong_guesses, encoded_word

def main():
    ascii_banner = pyfiglet.figlet_format("Welcome to Hangman!")
    print(bcolors.OKGREEN + ascii_banner + bcolors.ENDC)
    player_name = get_name()
    print("Welcome to Hangman,", player_name)
    level = get_level()
    word = get_word(words, level)
    original_word = get_word(words, level)
    encoded_word = re.sub('[0-9a-zA-Z]', '_', word)
    print(word) # Print selected word
    print(encoded_word) # Print word with _
    max_wrong_guesses = 21 # Must be every 7
    wrong_guesses = 0 # Starting value
    guess_counter = 0 # Starting value for loop
    print(HANGMAN[0]) # Starting Hangman
    while wrong_guesses < max_wrong_guesses and "_" in encoded_word:
        hidden_letters = guess_letter(word, encoded_word, level, wrong_guesses, guess_counter)
        wrong_guesses = hidden_letters[0]
        encoded_word = hidden_letters[1]
        index = int(wrong_guesses / get_hangman(max_wrong_guesses))
        print(HANGMAN[index])
        print(hidden_letters[1], hidden_letters[0])
    if wrong_guesses == max_wrong_guesses:
        decision = input("So sorry, you've failed! Do you want to play again? (y/n) ")
        if decision == "y":
            main()
    else:
        decision = input("Congratulations, you've won the game! Do you want to try again? (y/n)")
        if decision == "y":
            main()

        
        




if __name__ == '__main__':
    main()
