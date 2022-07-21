"""in a file called lines.py:
    implement a program that:
        expects exactly one command-line argument(the name (or path) of a Python file) and\
        outputs the number of lines of code in that file

        excluding comments and blank lines.

        If the user does not specify exactly one command-line argument or \
        if the specified file’s name does not end in .py, or \
        if the specified file does not exist:
            the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be
considered a comment.) Assume that any line that only contains whitespace is blank."""
import sys


def main():
    # Variable for storing the quantity of lines
    line_count = 0
    try:
        # Checking for <.py> at the end of the file
        if len(sys.argv) > 2:
            sys.exit('Only one command-line is allowed')
        if sys.argv[1][-3:] == '.py':
            with open(sys.argv[1]) as file:
                for line in file:
                    line = line.strip()
                    if not line.startswith('\n') and not line.startswith('#'):
                        print(line)
                print(line_count)

        else:
            sys.exit('The file must be a <.py> extension')
    except IndexError:
        sys.exit('There must be one command-line argument')
    except FileNotFoundError:
        sys.exit('The file specified must exist')


if __name__ == '__main__':
    main()

"""This was the output of the build-in 'check50' function"""
# :) lines.py exists
# :) lines.py exits given zero command-line arguments
# :) lines.py exits given a file without a .py extension
# :) lines.py exits given more than one command-line argument
# :) lines.py yields 3 given a file with 3 lines of code
# :) lines.py yields 4 given a file with 4 lines and whitespace
# :) lines.py yields 5 given a file with 5 lines, whitespace, and comments
# :) lines.py yields 9 given a file with 9 lines, whitespace, comments, and docstrings
# :) lines.py yields 2058 given 2058 lines of code in an open-source library file
