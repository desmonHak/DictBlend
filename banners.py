from colorama import Fore, ansi
from getpass import _raw_input

# ansi.clear_screen()

info_and_about = Fore.RED + '''
   ____     ___                    __       __             __ 
  /  _/__  / _/__    ___ ____  ___/ / ___ _/ /  ___  __ __/ /_
 _/ // _ \/ _/ _ \  / _ `/ _ \/ _  / / _ `/ _ \/ _ \/ // / __/
/___/_//_/_/ \___/  \_,_/_//_/\_,_/  \_,_/_.__/\___/\_,_/\__/ 
                                                            
''' + Fore.WHITE + '''
DictBlend is a Python script that provides various functions for social engineering and dictionary creation. 
It is designed to assist security professionals in assessing and improving security awareness. 
This toolkit includes features like generating permutations of words, 
conducting a social engineering questionnaire, 
exporting results to a file, and generating an alphabet wordlist.

Usage:
- Run the script by executing the following command:
  Example: python3 dictBlend.py

- Select an option from the menu:
  1. One Word - All Ways: Generates all possible forms of a single word.
  2. Social Engineering Questionnaire: Conducts a questionnaire to gather information.
  3. Generator from own words: Generates combinations from user-provided words.
  4. Generate alphabet wordlist: Generates combinations of the alphabet.

- Follow the prompts and input the required information.

- For option 1, the script will generate and export all possible forms of the input word.
- For option 2, the script will conduct a questionnaire and export the collected data.
- For option 3, the script will generate combinations from user-provided words and export them.
- For option 4, the script will generate combinations of the alphabet.

Note:
- This toolkit is created for educational and ethical use only.
- It includes functions for word permutation, data collection, and file export.
- Output files are created in the current working directory.
- Input options are validated to prevent errors and guide the user.

''' + Fore.RESET

banner = Fore.GREEN + """

██████╗ ██╗ ██████╗████████╗██████╗ ██╗     ███████╗███╗   ██╗██████╗ 
██╔══██╗██║██╔════╝╚══██╔══╝██╔══██╗██║     ██╔════╝████╗  ██║██╔══██╗
██║  ██║██║██║        ██║   ██████╔╝██║     █████╗  ██╔██╗ ██║██║  ██║
██║  ██║██║██║        ██║   ██╔══██╗██║     ██╔══╝  ██║╚██╗██║██║  ██║
██████╔╝██║╚██████╗   ██║   ██████╔╝███████╗███████╗██║ ╚████║██████╔╝
╚═════╝ ╚═╝ ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ 
                                                                         
        
                                 V1.3
       
                         BY TOMAS ILLUMINATI     

""" + Fore.RED + "   (This tool was created for educational and ethical use only.)   " + Fore.RESET
separator = Fore.BLUE + "\n------------------------------------------------------------------------" + Fore.RESET

def init_menu():
    print( Fore.YELLOW + """
        \n[0] exit program
        \n[1] One Word - All Ways  
        \n[2] Social Engineering Questionnaire  
        \n[3] Generator through strings  
        \n[4] Generate alphabet wordlist  
        \n[5] Info & About  
    """)
    option = 0
    while True:
        try:
            option =  int(_raw_input( "\n" + Fore.YELLOW + ">>> " + Fore.RESET))
            if option > 5 or option < 0: raise ValueError("Valor no dentro del rango 0 - 5")
            break
        except ValueError: print("{}[{}*{}] This option was not in the menu or is not a valid number.{}".format(Fore.WHITE, Fore.RED, Fore.WHITE, Fore.LIGHTRED_EX) + Fore.RESET)
    return option

def create_file(data):
    file_name = _raw_input(Fore.YELLOW + "\n[-] Insert the output file name (without extension): " + Fore.RESET) + ".txt"    
    with open(file_name, 'w') as file:
        for line in data:
            if isinstance(line, tuple):
                line = "".join(line)
            file.write(line + '\n')
    print(Fore.YELLOW + '\n[!] File "{}" has been created successfully.'.format(file_name) + Fore.RESET)

def questionnaire():
    info = list()
    print( Fore.CYAN + "\n[!] Please answer the following questionnaire (Place a [ - ] for non-response)" + Fore.RESET)
    info.append(_raw_input( Fore.CYAN + "\n[-] Target Name: "                   + Fore.RESET))
    info.append(_raw_input( Fore.CYAN + "\n[-] Target Lastname: "               + Fore.RESET))
    info.append(_raw_input( Fore.CYAN + "\n[-] Target Father Name: "            + Fore.RESET))
    info.append(_raw_input( Fore.CYAN + "\n[-] Target Mother Name: "            + Fore.RESET))
    info.append(_raw_input( Fore.CYAN + "\n[-] Target Nickname: "               + Fore.RESET))
    info.append(_raw_input( Fore.CYAN + "\n[-] Target Pet Name: "               + Fore.RESET))
    info.append(_raw_input( Fore.CYAN + "\n[-] Target child name: "             + Fore.RESET))
    info.append(_raw_input( Fore.CYAN + "\n[-] Target ID: "                     + Fore.RESET))
    info.append(_raw_input( Fore.CYAN + "\n[-] Target Birthday (MMDDYYYY): "    + Fore.RESET))
    for data in _raw_input( Fore.CYAN + "\n[-] Other info separate by (,) without spaces: " + Fore.RESET).strip().split(","): info.append(data)

    info = list(dict.fromkeys(info).keys())
    try: info.remove("-")
    except: pass

    return info