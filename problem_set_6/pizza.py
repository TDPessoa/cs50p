"""In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path)
of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at
pypi.org/project/tabulate. Format the table using the library’s grid format. If the user does not specify exactly one
command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist,
the program should instead exit via sys.exit."""

import sys
import tabulate


def main():
    tabl = []
    try:
        if len(sys.argv) > 2:
            sys.exit('Only one command line argument is allowed.')

        if sys.argv[1][-4:] == '.csv':
            with open(sys.argv[1]) as csv_file:
                for c in csv_file:
                    row = c.strip().rstrip().split(',')
                    tabl.append(row)
                print(tabulate.tabulate(tabl, headers='firstrow', tablefmt='grid'))

        else:
            sys.exit('The file extension must be <.csv>')

    except IndexError:
        sys.exit('A file must be specified in the command line')

    except FileNotFoundError:
        sys.exit('The file must exist for it to be open')


if __name__ == '__main__':
    main()

"""This was the output of the build-in 'check50' function"""
# :) pizza.py exists
# :) pizza.py exits given no command-line arguments
# :) pizza.py exits given non-existent file
# :) pizza.py exits given non-csv file
# :) pizza.py exits given too many command-line arguments
# :) pizza.py renders prices from sicilian.csv
# :) pizza.py renders prices from regular.csv
