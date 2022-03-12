import random
from colorama import Fore


def answer(get_sol=False):
    '''
    generates the solution list and assigns a solution for a given game instance.
    '''
    with open("solutions.txt") as sol:
        word_list_unformatted = sol.readlines()
        word_list = [w.strip().upper() for w in word_list_unformatted]

    solution = random.choice(word_list).upper()
    
    if get_sol:
        return solution
    else: return word_list
    

def valid():
    '''
    generates the valid word list
    '''
    with open("valid_words.txt") as valid_words:
        valid_words_list_unformatted = valid_words.readlines()
        valid_words_list = [v.strip().upper() for v in valid_words_list_unformatted]

    return valid_words_list


def input_word():
    '''
    user inputs a word and it check to see whether it is valid.
    '''
    valid_word_list = valid()
    sol_word_list = answer()
    word = input(Fore.BLUE + "Input a word: "+ Fore.RESET)
    chosen_word = word.strip().upper()

    if len(chosen_word) == 5:
        if chosen_word in (set(valid_word_list + sol_word_list)):
            return chosen_word
        else:
            print(Fore.RED + "Please input a valid word" + Fore.RESET)
            return input_word()
    else:
        return input_word()


def letters_info(letters,green,yellow,red):

    for letter in letters:
        if letter in green:
            print(Fore.GREEN + letter + Fore.RESET, end = " ")
        elif letter in yellow:
            print(Fore.YELLOW + letter + Fore.RESET, end = " ")
        elif letter in red:
            print(Fore.RED + letter + Fore.RESET, end = " ")
        else:
            print(Fore.WHITE + letter + Fore.RESET, end = " ")
    print("\n")




