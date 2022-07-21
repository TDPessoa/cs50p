"""In a file called scourgify.py, implement a program that:

    Expects the user to provide two command-line arguments:
        the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house,
        and
        the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.

    Converts that input to that output, splitting each name into a first name and last name. Assume that each student
will have both a first name and last name.
        If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program
should exit via sys.exit with an error message."""

import sys


def main():
    final = []
    try:
        if len(sys.argv) == 3:
            if ('before' in sys.argv[1]) and ('.csv' in sys.argv[1]) and \
                    ('after' in sys.argv[2]) and ('.csv' in sys.argv[2]):
                with open(sys.argv[1]) as before:
                    for line in before:
                        line = line.rstrip().replace('"', '').split(',')
                        if len(line) == 3:
                            row = f'{line[1].strip()},{line[0].strip()},{line[2].strip()}\n'

                        else:
                            row = f'first,last,house\n'

                        final.append(row)

                    before.close()

                with open(sys.argv[2], 'w') as after:
                    for line in final:
                        after.write(str(line))

                    after.close()
                    sys.exit()
            else:
                sys.exit('1It must be specified 2(two) VALID command-line arguments.')

        else:
            sys.exit('2It must be specified 2(two) VALID command-line arguments.')

    except IndexError:
        sys.exit('3It must be specified 2(two) VALID command-line arguments.')

    except FileNotFoundError:
        sys.exit('The first file in command-line must exist.')


if __name__ == '__main__':
    main()

"""This was the output of the build-in 'check50' function"""
# :) scourgify.py exists
# :) scourgify.py exits given no command-line arguments
# :) scourgify.py exits given too few command-line arguments
# :) scourgify.py exits given too many command-line arguments
# :) scourgify.py exits given invalid input file
# :) scourgify.py creates new CSV file
# :) scourgify.py cleans short CSV file
# :) scourgify.py cleans long CSV file
