import random

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

words = ["Marysia", "Asia", "Kasia", "Amadeusz", "Encyklopedia", "Jedenm"]

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

def get_name():
    player_name = input("Please enter your name. ")
    return player_name

def get_level():
    print("Please select level of difficulty: ")
    print(" 1 - Easy")
    print(" 2 - Medium")
    print(" 3 - Hard")
    level = int(input(""))
    while level > 3 or level <= 0:
        level = int(input("You have chosen wrong level, please try again. "))
        
    if level == 1:
        print("You've chosen easy level. ")
    elif level == 2:
        print("You've chosen medium level. ")
    else:
        print("You've chosen hard level. ")
    return int(level)

def get_word(words, level):

    word_number = random.randint(0, len(words) -1)
    word = words[word_number]

    if level == 1:
        while len(word) > 5:
            word_number = random.randint(0, len(words) -1)
            word = words[word_number]
        return word

    elif level == 2:
        while len(word) <= 5 or len(word) > 8:
            word_number = random.randint(0, len(words) -1)
            word = words[word_number]
        return word 

    else:
        while len(word) <= 8:
            word_number = random.randint(0, len(words) -1)
            word = words[word_number]
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
    



def main():
    print(bcolors.FAIL + "\t\tWelcome to Hangman!" + bcolors.ENDC)
    player_name = get_name()
    print("Welcome", player_name, "to Hangman. ")
    level = get_level()
    word = get_word(words, level)
    max_wrong_guesses = 21 # Must be every 7
    wrong_guesses = 0 # Starting value
    index = int(wrong_guesses / get_hangman(max_wrong_guesses))
    print(HANGMAN[index])
    # while wrong_guesses < max_wrong_guesses:
    #     if wrong_guesses < get_hangman(max_wrong_guesses):
        




if __name__ == '__main__':
    main()