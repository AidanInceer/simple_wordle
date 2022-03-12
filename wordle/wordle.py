from colorama import Fore
import wordle_logic


def main():
    # Initlize lists and solution
    num_guesses  = 0
    attempts = []
    qwer = ["Q","W","E","R","T","Y","U","I","O","P"]
    asdf = ["A","S","D","F","G","H","J","K","L"]
    zxcv = ["Z","X","C","V","B","N","M"]
    solution = wordle_logic.answer(True)
    print("------------------------------")

    while True:
        green = []
        yellow = []
        red = []
        # initialise guessed word
        word = wordle_logic.input_word()
        attempts.append(word)
        guess_list = list(word)
        solution_list = list(solution)

        # print guessed word/s with colors
        for attempt in range(len(attempts)):
            print("\n")
            print("    ",end="")
            for letter in range(len(attempts[attempt])):
                if attempts[attempt][letter] == solution[letter]:
                    print(" " + Fore.GREEN + f"{attempts[attempt][letter]} " + Fore.RESET, end=" ")
                    green.append(attempts[attempt][letter])

                elif attempts[attempt][letter] in solution:
                    print(" " + Fore.YELLOW + f"{attempts[attempt][letter]} " + Fore.RESET, end=" ")
                    yellow.append(attempts[attempt][letter])

                else:
                    print(" " + Fore.RED + f"{attempts[attempt][letter]} " + Fore.RESET, end=" ")
                    red.append(attempts[attempt][letter])

        # letter information
        print("\n" + (5-num_guesses)*"\n     _   _   _   _   _\n")
        print("    ", end="")
        line1 = wordle_logic.letters_info(qwer,green,yellow,red)
        print("     ", end="")
        line2 = wordle_logic.letters_info(asdf,green,yellow,red)
        print("       ", end="")
        line3 = wordle_logic.letters_info(zxcv,green,yellow,red)
        print("------------------------------")

        # break if solution guessed
        if attempts[attempt] == solution:
            print(f"\n  You guessed the solution!\n\n\n\n")
            break

        # break statement if number of guesses exceeded
        if num_guesses >= 5:
            print(f"{Fore.RED}  You ran out of guesses!\n     The word was {solution}{Fore.RESET}\n\n\n\n")
            break

        # guesses incrementer
        num_guesses += 1


if __name__ == "__main__":
    main()
