"""In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be
-f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the
name of a font, the program should exit via sys.exit with an error message."""

from random import choice

import pyfiglet
import sys


def main():
    list_of_fonts = ['rectangles', 'slant', 'alphabet']
    try:
        if sys.argv[1] == '-f' or sys.argv[1] == '--font':
            if sys.argv[2] in list_of_fonts:
                message = str(input("Input:"))
                pyfiglet.print_figlet(message, sys.argv[2])
            else:
                sys.exit('Invalid usage')
        else:
            sys.exit('Invalid usage')

    except IndexError:
        message = str(input("Input:"))
        pyfiglet.print_figlet(message, choice(list_of_fonts))


main()

"""This was the output of the build-in 'check50' function"""
# :) figlet.py exists
# :) figlet.py exits given one command-line argument
# :) figlet.py exits given invalid first command-line argument
# :) figlet.py exits given invalid second command-line argument
# :) figlet.py renders slanted text
# :) figlet.py renders rectangular text
# :) figlet.py renders alphabet text
