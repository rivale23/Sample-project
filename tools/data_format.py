#!/usr/bin/env python

import os
import subprocess
import argparse
import glob
from pathlib import Path
import sys
import pdb
from colorama import Fore, Back, Style
from colorama import init

"""
This method checks forbidden keywords in file but ignores
standard constructs like int main(int argc, char** argv)
int setup(), int teardown () (used in unit testing ),
 and additionally prints the line where char is found
"""


def type_check(filename: str, str_types: str) -> int:
    intTokensToAvoid = ['main(int', 'main()', 'main', 'main(void)',
                        'setup()', 'teardown()', 'setup(void**', 'teardown(void**']
    intCount = 0
    output = Fore.BLUE + 'file: ' + Fore.RESET + str(filename) + '\n'
    file = open(filename, 'r')
    lines = file.readlines()
    line_num = 1
    for line in lines:
        tokens = line.split()
        for str_type in str_types:
            t = [t for t in tokens if str_type in t]
            if(str_type in tokens):
                if(len(t) > 0 and t[0] in [str_type, str_type + '*', str_type + '**']):
                    idx = tokens.index(str_type)
                    if(idx + 1 < len(tokens) and (tokens[idx + 1] not in intTokensToAvoid)):
                        intCount += 1
                        output += Fore.RED + "Line " + str(line_num) + ": " + Fore.RESET + line.replace(str_type + " ",
                                                                                                        Fore.RED + str_type + " " + Fore.RESET)
        line_num += 1

    if(intCount > 0):
        output += Fore.CYAN + \
            str(intCount) + Fore.RESET + " violations found\n"
        print(output)

    return intCount


"""
This method walks through each file .c and .h in 
the directory and child directories avoiding 
archive, cmocka extern and build directories
and checks in the remaining files for 
'int', 'char', 'unsigned' and 'long int' 
keywords in project files. 

If any of the above keyword is found then the 
function prints the file name(s) and returns -1
"""


def check_data_types():
    print("searching for non EDR data types ...")
    errorsCount = 0
    errorsFiles = []

    forbidden_types = ["int", "char", "unsigned",
                       "float", "uint8", "uint16", "uint32"]
    for filename in (*Path('.').rglob('*.c'), *Path('.').rglob('*.h')):
        if(not("cmocka" in str(filename))):
            errors = type_check(filename, forbidden_types)
            if(errors > 0):
                errorsCount += errors
                errorsFiles.append(filename)

    print(Fore.RED + "*******************Errors found in the following files:*******************")
    for err_file in errorsFiles:
        print(str(err_file))

    if(errorsCount > 0):
        return 1

    return 0


if __name__ == '__main__':
    init(autoreset=True)
    sys.exit(check_data_types())
