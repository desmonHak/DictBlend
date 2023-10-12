from string import ascii_uppercase, ascii_lowercase
from itertools import permutations, product
from colorama import Fore, ansi
from colorama.ansi import clear_screen
from getpass import _raw_input
from sys import exit
from banners import *

if __name__ == "__main__":
    try:
        while True:
            clear_screen()
            print(separator + banner + separator)
            options = init_menu()
            
            clear_screen()
            if options == 0: exit(options)
            elif options == 1:
                wString = _raw_input(Fore.CYAN + "\n[-] Insert only one string: " + Fore.RESET).strip().split(" ")
                possible_forms = [''.join(p) for p in permutations(wString[0])]
                create_file(possible_forms)
            elif options == 2:
                wList =  questionnaire()
                clear_screen()
                print(separator + banner + separator + Fore.YELLOW + 
                    """\n[!] Do you want to set a maximum length for each string in the dictionary?
                    \n[!] If you don't do this, the file could exceed 5GB or more""" + separator + Fore.YELLOW + """
                    \n[1] Yes
                    \n[2] No """)
                answer = 0
                while True:
                    try:
                        answer = _raw_input(Fore.YELLOW +  "\n>>> ")
                        if answer > 2 or answer < 1: raise ValueError("Value not in range 1 - 2")
                        break
                    except ValueError: print("{}[{}*{}] The value can only be 1 or 2{}".format(Fore.WHITE, Fore.RED, Fore.WHITE, Fore.LIGHTRED_EX) + Fore.RESET)
                if answer == 1:
                    while True:
                        try: 
                            num = int(_raw_input(Fore.CYAN + "\nSet the maximum char lenght: "))
                            break
                        except ValueError: print("{}[{}*{}] The value can only be a number{}".format(Fore.WHITE, Fore.RED, Fore.WHITE, Fore.LIGHTRED_EX) + Fore.RESET)
                    create_file([string for string in product(wList, repeat=len(wList)) if len(string) <= num])

            elif options == 3:
                info = list(dict.fromkeys(_raw_input(Fore.CYAN + "\n[!] Please insert info separate by (,) without spaces: \n>>> " + Fore.RESET).strip().split(",")).keys())
                create_file(product(info, repeat=len(info)))
            elif options == 4:
                range_numbers = [0, len(ascii_lowercase + ascii_uppercase)]
                while True:
                    try: 
                        range_numbers[1] = int(_raw_input(Fore.YELLOW + "\n[-] lenght (max {}): ".format(len(ascii_lowercase))))
                        if range_numbers[1] > len(ascii_lowercase) or range_numbers[1] < range_numbers[0]:
                            raise ValueError("The value exceeds the maximum")
                        create_file(product(ascii_lowercase + ascii_uppercase, repeat=range_numbers[1]))
                        break
                    except ValueError: print("{}[{}*{}] The value can only be a number{}".format(Fore.WHITE, Fore.RED, Fore.WHITE, Fore.LIGHTRED_EX) + Fore.RESET)
            elif options == 5: 
                print(info_and_about) 
                _raw_input("press une key...")
    except KeyboardInterrupt:
        print("Exit program...")
        exit(0)