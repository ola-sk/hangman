def is_number(str):
    if isinstance(str, (int, float)) == True:
        return True
    else:
        return False


def is_valid_operator(operator):
    if operator == "+" or operator == "-" or operator == "*" or operator == "/":
        return True
    else:
        return False


def ask_for_a_number():
    try:
        number = float(input("Podaj liczbę "))
        if is_number(number):
            return number
    except ValueError:
        print ("Błedna wartość, nastąpił powrót do początku. ")


def ask_for_an_operator():
    operator = input("Podaj operatora")
    if is_valid_operator(operator):
        return operator
    else:
        print("Błędny operator, nastąpił powrót do początku. ")


def calc(operator, a, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            print("Wartość nie może być 0")
            return None
        return a / b
    else:
        return None

def internal_calculator():
    number_one = ask_for_a_number()
    if is_number(number_one) == False:
        print("Podałeś nieprawidłową cyfrę, podaj prawidłowe dane. ")
        internal_calculator()
            
    operator = ask_for_an_operator()
    while is_valid_operator == False:
        print("Podałeś złego operatora, podaj prawidłowe dane. ")
        internal_calculator()
            
    number_two = ask_for_a_number()
    while is_number(number_two) == False:
        print("Podałeś złą liczbę, podaj prawidłowe dane. ")
        internal_calculator()

    print("Wynik działania", number_one, operator, number_two, "=", calc(operator, number_one, number_two))
    decision = input("Czy chcesz ponowić kalkulację? (tak/nie) ")
    if decision == "tak":
        internal_calculator()

def simple_calculator():
    print("Witaj w kalkulatorze.")
    internal_calculator()
    
if __name__ == '__main__':
    simple_calculator()