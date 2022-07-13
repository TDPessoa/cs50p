"""In a file called game.py, implement a program that:

    Prompts the user for a level, . If the user does not input a positive integer, the program should prompt again.
    Randomly generates an integer between 1 and , inclusive, using the random module.
    Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user
again.
        If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
        If the guess is larger than that integer, the program should output Too large! and prompt the user again.
        If the guess is the same as that integer, the program should output Just right! and exit."""


from sys import exit
from random import randint as rint


def main():
    # Collecting level input
    while True:
        try:
            level = int(input('Level:'))

            if level >= 1:
                break

            else:
                pass

        except ValueError:
            pass

    # Setting level value as 'x'
    x = rint(1, level)

    # Collecting guess input
    while True:
        try:
            guess = int(input('Guess:'))

            # Verifier for positive value
            if guess > 0:
                # 'closing in' conditionals
                if guess < x:
                    print('Too small!')
                    pass

                elif guess == x:
                    exit('Just right!')

                elif guess > x:
                    print('Too large!')
                    pass

            else:
                pass

        except ValueError:
            pass


main()

"""This was the output of the build-in 'check50' function"""
# :) game.py exists
# :) game.py rejects non-numeric level
# :) game.py rejects out-of-range level
# :) game.py accepts valid level
# :) game.py rejects non-numeric guess
# :) game.py rejects out-of-range guess
# :) game.py outputs "Too large!" when guess is too large
# :) game.py outputs "Just right!" when guess is correct
# :) game.py outputs "Too small!" when guess is too small
