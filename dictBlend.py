from string import ascii_uppercase, ascii_lowercase
from itertools import permutations, product
from colorama import Fore, ansi
from colorama.ansi import clear_screen
from getpass import _raw_input
from sys import exit
from banners import *

class App():
    def __init__(self):
        self.options = {
            0: self.exit_program,
            1: self.one_word,
            2: self.questionnaire,
            3: self.generator_strings,
            4: self.generate_wordlist,
            5: self.info,
            }
    
    def print_menu(self):
        print( Fore.YELLOW + """
            \n[0] exit program
            \n[1] One Word - All Ways  
            \n[2] Social Engineering Questionnaire  
            \n[3] Generator through strings  
            \n[4] Generate alphabet wordlist  
            \n[5] Info & About  
        """)

    def select_option(self):
        self.print_menu()
        while True:
            try:
                option =  int(_raw_input( "\n" + Fore.YELLOW + ">>> " + Fore.RESET))
                if option > 5 or option < 0: raise ValueError("Valor no dentro del rango 0 - 5")
                break
            except ValueError: print("{}[{}*{}] This option was not in the menu or is not a valid number.{}".format(Fore.WHITE, Fore.RED, Fore.WHITE, Fore.LIGHTRED_EX) + Fore.RESET)
        return option

    def main(self):
        try:
            while True:
                clear_screen()
                print(separator + banner + separator)
                option = self.select_option()
                self.options[option]()
        except KeyboardInterrupt:
            self.exit_program()
    
    # App Functions
    def exit_program(self):
        print("Exit program...")
        exit(0)

    def one_word(self):
        wString = _raw_input(Fore.CYAN + "\n[-] Insert only one string: " + Fore.RESET).strip().split(" ")
        possible_forms = [''.join(p) for p in permutations(wString[0])]
        create_file(possible_forms)

    def questionnaire(self):
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
                answer = int(_raw_input(Fore.YELLOW +  "\n>>> "))
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

    def generator_strings(self):
        info = list(dict.fromkeys(_raw_input(Fore.CYAN + "\n[!] Please insert info separate by (,) without spaces: \n>>> " + Fore.RESET).strip().split(",")).keys())
        create_file(product(info, repeat=len(info)))

    def generate_wordlist(self):
        range_numbers = [0, len(ascii_lowercase + ascii_uppercase)]
        while True:
            try: 
                range_numbers[1] = int(_raw_input(Fore.YELLOW + "\n[-] lenght (max {}): ".format(len(ascii_lowercase))))
                if range_numbers[1] > len(ascii_lowercase) or range_numbers[1] < range_numbers[0]:
                    raise ValueError("The value exceeds the maximum")
                create_file(product(ascii_lowercase + ascii_uppercase, repeat=range_numbers[1]))
                break
            except ValueError: print("{}[{}*{}] The value can only be a number{}".format(Fore.WHITE, Fore.RED, Fore.WHITE, Fore.LIGHTRED_EX) + Fore.RESET)

    def info(self):
        print(info_and_about) 
        _raw_input("press une key...")

if __name__ == "__main__":
    myapp = App()
    myapp.main()