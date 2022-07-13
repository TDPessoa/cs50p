"""In a file called professor.py, implement a program that:

    Prompts the user for a level, . If the user does not input 1, 2, or 3, the program should prompt again.
    Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer
with  digits. No need to support operations other than addition (+).
    Prompts the user to solve each of those problem. If an answer is not correct (or not even a number), the program
should output EEE and prompt the user again, allowing the user up to three tries in total. If the user has still not
answered correctly after three tries, the program should output the correct answer.
    The program should ultimately output the user’s score, a number out of 10.
    Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level
and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or
raises a ValueError if level is not 1, 2, or 3:

        import random


        def main():
            ...


        def get_level():
            ...


        def generate_integer(level):
            ...


        if __name__ == "__main__":
            main()"""

from random import randint as rint


def main():
    level = get_level()
    correct_count = 0
    # Initializing problems
    for i in range(10):
        # Generating integers
        x = generate_num(level)
        y = generate_num(level)
        s = x + y
        for j in range(3):
            try:
                answer = int(input(f'{x} + {y} = '))
                if answer == s:
                    correct_count += 1
                    break

                else:
                    print('EEE')
                    pass

            except ValueError:
                print('EEE')
                pass

        # At the count of 3 mistakes, the program outputs the correct answer
        print(f'{x} + {y} = {s}')

    # After all the problems have been displayed and finished, its prompted the score
    print(f'Score: {correct_count}')
    exit()


# Just a function to ask the user for a integer from 1 to 3.
def get_level():
    while True:
        try:
            level = int(input('Level:'))
            if 1 <= level <= 3:
                break

            else:
                pass

        except ValueError:
            pass

    return level


# Number generator, adds one decimal place by the value of 'level'
def generate_num(level):
    num = 0
    if level == 1:
        num = rint(0, 9)

    elif level == 2:
        num = rint(10, 99)

    elif level == 3:
        num = rint(100, 999)

    return num


if __name__ == '__main__':
    main()

"""This was the output of the build-in 'check50' function"""
# :) professor.py exists
# :) Little Professor rejects level of 0
# :) Little Professor rejects level of 4
# :) Little Professor rejects level of one
# :) Little Professor accepts valid level
# :) At Level 1, Little Professor generates addition problems using 0–9
# :) At Level 2, Little Professor generates addition problems using 10–99
# :) At Level 3, Little Professor generates addition problems using 100–999
# :) Little Professor generates 10 problems before exiting
# :) Little Professor displays number of problems correct
# :) Little Professor displays EEE when answer is incorrect
# :) Little Professor shows solution after 3 incorrect attempts
