"""This will be submitted as my final project to Harvard's CS50p"""

from random import randint, choice, seed
from sys import argv


def main():
    # This try statement is to treat exceptions
    try:
        # Setting the return value of initializer to a variable for simplicity
        arguments = initializer(argv)
        # Verifying the options the user has chosen
        #   User chose to play
        if arguments[0] == 'p':
            # Variable to store the run's score
            _score = 0
            # Level chosen, ie. 1, 2, 3, 4
            level = int(arguments[1])
            # The game script starts
            if 1 <= level <= 4:
                # Variables for counting runs and number of hearts(user's second, third and fourth chance for 'endless'
                # runs)
                count = 1
                hearts = 3
                # Infinite loop
                while True:
                    # Generating problem
                    v1, v2, op = generate(level)
                    # A div
                    print('\n', '-'*100)
                    # Output for the problem, input for the answer and counting the questions done
                    print(f'Problem {count}: \t{v1} {op} {v2} = ??')
                    user_answer = int(input("Answer:"))
                    count += 1
                    # Answer checker
                    if question(v1, v2, op, user_answer):
                        _score += 1
                        print('Correct!')

                    # Wrong answer was given
                    else:
                        # When in "endless" mode the hearts are subtracted
                        if level == 4:
                            # Decreasing the value of hearts
                            hearts -= 1
                            # Printing out incorrect answer message
                            print(f'Wrong answer, you have {hearts} hearts left')

                        # No hearts left
                        if hearts == 0:
                            break

                    # "Normal" game mode breaker
                    if (1 <= level <= 3) and (count > 10*level):
                        break

                # At the end of the run, the argument 'p' will be used by score to register the rank
                score(level, arguments[0], _score)

        #   User chose to print the score
        elif arguments[0] == 's':
            level = arguments[1]
            score(level, 's')

        #   User chose to see the program usage
        elif arguments[0] == 'h':
            print('usage: py project.py [ options ]\n    options:\n        -p, --play [ level ]\n            level:\n'
                  '                1 or "easy"         10 Problems of addition and subtraction\n                2 or '
                  '"medium"       20 Problems of addition, subtraction and multiplication\n                3 or "hard"'
                  '         30 Problems of addition, subtraction, multiplication and division\n                4 or '
                  '"endless"      Endless quantity of Medium difficulty but, if three incorrect answers where given, '
                  'the run ends\n        -s, --score [ level ]\n            level:\n                1, 2, 3, 4        '
                  '  Will print in Terminal the Top 10 highest scores for that level\n        -h, --help', sep='')

    except ValueError or IndexError:
        print("Please, refer to: python project.py [-h, --help]")


def initializer(command):
    """
    Will handle the command_line argument and return the required way.

    :param command: str, to be extracted the values
    :return:  a str and/or an int =>    -p, --play  -> ['p', 'level']
                                        -s, --score -> ['s', 'level']
                                        -h, --help  -> ['h']
    """
    # Setting the str given to another variable as list type
    if type(command) is str:
        phrase = command.split(' ')

    else:
        phrase = command

    # Checking for 2 or 3 command-line arguments
    if 1 < len(phrase) <= 3:
        # Declaring a list to be returned and a list with the names of difficulties
        arguments = []
        levels = ['easy', 'medium', 'hard', 'endless']
        # Checking for {'-h', '--help'} in the second argument
        if phrase[1] == '-h' or phrase[1] == '--help':
            arguments.append('h')

        # Checking for {'-p', '--play'} in the second argument and if the value given is an int between 0 and 5
        elif phrase[1] == '-p' or phrase[1] == '--play':
            # When the script finds the 'play' option, it will add 'p' to arguments
            arguments.append('p')

        # Checking for {'-s', '--score'} in the second argument and if the value is between 0 and 5
        elif phrase[1] == '-s' or phrase[1] == '--score':
            # When the script finds the 'score' option, it will add 's' to arguments
            arguments.append('s')

        # Command-line has errors
        else:
            raise ValueError

        # Now to treat the level value
        if arguments[0] != 'h':
            # For alphabetical values
            if phrase[2].isalpha():
                # Starting a loop
                for c in range(4):
                    # When the correct value is found it returns the index plus one
                    if phrase[2] == levels[c]:
                        arguments.append(c + 1)
                        # And breaks
                        break

                    # If the Index was surpassed, it raises valueerror
                    if c == 3:
                        raise ValueError

            # For integer values
            elif 1 <= int(phrase[2]) <= 4:
                arguments.append(int(phrase[2]))

            # Not sure if there is a chance, but, just in case
            else:
                raise ValueError

    else:
        raise ValueError

    return arguments


def generate(level, test=False):
    """
    Will generate the values of two variables and choose the operator

    Will always list the greater value as num1.
    When:
        In medium difficulty:
            Will set the multiplier as it's decimal case.
        In hard difficult:
            Will set the divisor as it's decimal case
                And re-draw if the answer isn't an integer.
            Will set the multiplier as its tenths and decimal cases.

    :param level:   int, to be used as template for drawing the values.
    :param test:    Bool, only used in test_project
    :return:        int | int | str -> as: num1, num2, operator
    """
    # Setting test seed
    if test:
        seed(2)

    # Soothing endless mode
    if level == 4:
        level = 2

    # Setting minimum and maximum values
    _min, _max = 1, int('9' * level)
    # Setting the operators list, addition and subtraction for level 1
    operators = ['+', '-']
    # level 1 plus multiplication for level 2
    if level > 1:
        operators.append('*')

    # level 2 plus division for level 3
    if level > 2:
        operators.append('/')

    while True:
        # Generating values of x, y and op
        x = randint(_min, _max)
        y = randint(_min, _max)
        op = choice(operators)
        # Checking if second value is greater than first
        if x < y:
            place_holder = x
            x = y
            y = place_holder

        # division and multiplication are way harder if are greater then 10
        if op == '*' and y > 100:
            y = y // 100

        # "
        elif op == '*' and y > 10:
            y = y // 10

        # "
        if op == '/' and y > 100:
            y = y // 100

        # "
        elif op == '/' and y > 10:
            y = y // 10

        # Checking for a decimal division
        if op == '/' and x % y != 0:
            pass

        # If it's not a division or if it's a division but the result is an integer.
        else:
            break

    return x, y, op


def question(x, y, op, answer):
    """
    Will receive the values and operator of the problem with the answer to be verified.

    :param x:       int, first value of the problem
    :param y:       int, second value of the peoblem
    :param op:      str, from ('+', '-', '*', '/')
    :param answer:  int, user's inputted answer
    :return:        Bool -> if f'x {op} y' == answer
    """
    if op == '+':
        return answer == x + y

    elif op == '-':
        return answer == x - y

    elif op == '*':
        return answer == x * y

    elif op == '/':
        return answer == x / y


def score(level, action, _score=None):
    """
    Will open the score file to the specified level and record the scored points or print out the current stored rank.
    If the score_file has anything out of the ordinary(ie. less then 10 lines or was not found) it will be re-writen

   :param level: int -> 1, 2, 3, 4
   :param action: str -> 's' -> reads score | 'p' -> records score | 'r' -> restores score
   :param _score: None | int
   :return: None
    """
    try:
        # User has finished a run and the score will be stored
        if action == 'p':
            # opening the file in read mode for extracting the values
            with open(f'scores/score_{level}.txt', 'r') as score_list:
                # Infinite Loop for name collection
                while True:
                    user_name = str(input('Please, enter 3 letters so I can store your score: ')).strip()
                    # Checking for at least 3 letters in the name
                    if len(user_name) > 2 and user_name.isalpha():
                        # Collecting only the first 3 letters in name and setting to uppercase
                        user_name = user_name[:3].upper()
                        break

                    # Message for the "re-run"
                    print('Please, try again...')

                # Setting the line that will be stored
                current_score = f'{user_name} {_score}\n'
                # Setting an list to collect the scores
                scores = []
                # Passing through the list of scores to search for the position the user has got
                for n in score_list:

                    # A score lower then the user's was found
                    if int(n.split(' ')[1]) < _score and current_score != 0:
                        # The user's line is appended to the list
                        scores.append(current_score)
                        # The variable is changed to something meaningless to avoid duplicates
                        current_score = 0

                    # The scores if not one place lower then the user's will be appended to the list
                    scores.append(n)

                # Finished collecting data
                score_list.close()

            # Opening the file as write mode
            with open(f'scores/score_{level}.txt', 'w') as score_list:
                # passing through the first 10 itens in the collected scores
                for n in range(10):
                    # Adding each line
                    score_list.write(scores[n])

                # Finished writing in the file
                score_list.close()

        # User chose to print-out the scores
        if action == 's':
            # Opening the file
            with open(f'scores/score_{level}.txt', 'r') as scores:
                # List for collecting the information
                score_list = []
                # Passing through each line in the file
                for n in scores:
                    # Collecting the line to the list
                    score_list.append(n)

                # Starting the printing of the scores
                print('-'*100, '\nHighest Scores!!!\n', '-'*100)
                # Printing each score in the list
                for i in range(10):
                    print(f'{i + 1}\t{score_list[i].split(" ")[0]}\t{score_list[i].split(" ")[1]}', end='')

                # Finished printing
                scores.close()

        # Something went wrong with the files, this will "refresh" the files to default
        if action == 'r':
            # Oppening the broken file as write mode
            with open(f'scores/score_{level}.txt', 'w') as broken:
                # Loop for re-writtin the content
                for _ in range(10):
                    # Default 0 values
                    broken.write('DFT 0\n')

                # Closing broken file
                broken.close()

    # Handling exceptions that may caused the score function to fail
    except FileNotFoundError:
        # Warning message, just in case the user has tinkered with the scores and don't want the program to erase all
        print('WARNING-WARNING-WARNING-WARNING\nSomething is wrong with the file and it need to be restored '
              'to default!!!\nDo you agree with this action?')
        # Infinite loop to receive a assertive answer from the user
        while True:
            checker = str(input('[yes, no]: '))
            # The user has chosen to erase the data, the loop ends and the function is executed
            if checker == 'yes':
                break
            # The user has chosen to not erase, the program exits
            elif checker == 'no':
                exit()

        score(level, 'r')

    except IndexError:
        # Warning message, just in case the user has tinkered with the scores and don't want the program to erase all
        print('WARNING-WARNING-WARNING-WARNING\nSomething is wrong with the file and it need to be restored '
              'to default!!!\nDo you agree with this action?')
        # Infinite loop to receive a assertive answer from the user
        while True:
            checker = str(input('[yes, no]: '))
            # The user has chosen to erase the data, the loop ends and the function is executed
            if checker == 'yes':
                break
            # The user has chosen to not erase, the program exits
            elif checker == 'no':
                exit()

        score(level, 'r')


if __name__ == '__main__':
    main()
