"""This will be the test_file for the script: project.py"""

from pytest import raises
from project import initializer
from project import generate
from project import question
from project import score


# Assert that the initializer returns the correct values
def test_initializer():
    # Asserting {-p, --play}
    assert initializer("file_name -p 1") == ['p', 1]
    assert initializer("file_name --play 1") == ['p', 1]
    # Asserting {-s, --score}
    assert initializer("file_name -s 2") == ['s', 2]
    assert initializer("file_name --score 3") == ['s', 3]
    # Asserting {-h, --help}
    assert initializer("file_name -h") == ['h']
    assert initializer("file_name --help") == ['h']
    # Asserting {1, 2, 3, 4}
    assert initializer("file_name -p 2") == ['p', 2]
    assert initializer("file_name -s 3") == ['s', 3]
    assert initializer("file_name -s 4") == ['s', 4]
    # Asserting {'easy', 'medium', 'hard', 'endless'}
    assert initializer("file_name -p easy") == ['p', 1]
    assert initializer("file_name -s medium") == ['s', 2]
    assert initializer("file_name -s hard") == ['s', 3]
    assert initializer("file_name -s endless") == ['s', 4]
    # Asserting Exceptions
    #   ValueError's
    with raises(ValueError):
        initializer("file_name -s n")
    with raises(ValueError):
        initializer("file_name -s 5")
    with raises(ValueError):
        initializer("file_name -s -1")
    with raises(ValueError):
        initializer("file_name -e 1")
    with raises(ValueError):
        initializer("file_name --error 1")
    #   IndexError's
    with raises(ValueError):
        initializer("file_name -s 1 another")
    with raises(ValueError):
        initializer("file_name")
    with raises(ValueError):
        initializer("")


# Asserting generate() returns correct values
def test_generate():
    # Some variables for checking
    operators = ['+', '-', '*', '/']
    # Asserting operators
    assert generate(1)[2] in operators
    assert generate(2)[2] in operators
    assert generate(3)[2] in operators
    # Asserting indexes 0 and 1 are integers and 2 is string
    assert (type(generate(1)[0]) is int) and (type(generate(1)[1]) is int) and (type(generate(1)[2]) is str)
    assert (type(generate(2)[0]) is int) and (type(generate(2)[1]) is int) and (type(generate(2)[2]) is str)
    assert (type(generate(3)[0]) is int) and (type(generate(3)[1]) is int) and (type(generate(3)[2]) is str)
    # Asserting generate will work with preset seed
    assert generate(1, True) == (2, 1, '+')
    assert generate(2, True) == (12, 8, '+')
    assert generate(3, True) == (979, 884, '+')
    # Asserting indexes 0 is greater then 1
    #   Variable assign is needed because if used as in #3 the values will be from different "runs" of the function
    #   And may have different results
    values = generate(1)
    assert values[0] >= values[1]
    values = generate(2)
    assert values[0] >= values[1]
    values = generate(3)
    assert values[0] >= values[1]


# Asserting question() works propperly
def test_question():
    # Asserting addition answers
    #   Correct
    assert question(2, 1, '+', 3)
    assert question(22, 11, '+', 33)
    assert question(222, 111, '+', 333)
    #   Incorrect
    assert not question(2, 1, '+', 0)
    assert not question(22, 11, '+', 0)
    assert not question(222, 111, '+', 0)
    # Asserting subtraction answers
    #   Correct
    assert question(2, 1, '-', 1)
    assert question(22, 11, '-', 11)
    assert question(222, 111, '-', 111)
    #   Incorrect
    assert not question(2, 1, '-', 0)
    assert not question(22, 11, '-', 0)
    assert not question(222, 111, '-', 0)
    # Asserting multiplication answers
    #   Correct
    assert question(2, 1, '*', 2)
    assert question(22, 11, '*', 242)
    assert question(222, 111, '*', 24642)
    #   Incorrect
    assert not question(2, 1, '*', 0)
    assert not question(22, 11, '*', 0)
    assert not question(222, 111, '*', 0)
    # Asserting division answers
    #   Correct
    assert question(2, 1, '/', 2)
    assert question(22, 11, '/', 2)
    assert question(222, 111, '/', 2)
    #   Incorrect
    assert not question(2, 1, '/', 0)
    assert not question(22, 11, '/', 0)
    assert not question(222, 111, '/', 0)
    # Assert using generate
    #   Variables
    #       Generate(1, 1) => [2, 1, '+']
    x, y, op = generate(1, True)
    answer = x + y
    assert question(x, y, op, answer)
    #       Generate(2, 2) => [12, 8, '+']
    x, y, op = generate(2, True)
    answer = x + y
    assert question(x, y, op, answer)
    #       Generate(3, 3) => [979, 884, '+']
    x, y, op = generate(3, True)
    answer = x + y
    assert question(x, y, op, answer)


# Asserting score() works propperly
def test_score():
    # Reseting the score test file
    score('test', 'r')
    # Testing the score_test.txt file
    with open('scores/score_test.txt', 'r') as test:
        for _ in range(10):
            line = test.readline().strip('\n')
            assert line == 'DFT 0'
        test.close()

    # Testing 'refreshing' the file
    with open('scores/score_test.txt', 'w+') as test:
        for _ in range(10):
            test.write('test test test\n')

        for _ in range(10):
            line = test.readline().strip('\n')
            assert line != 'DFT 0'

        test.close()

    score('test', 'r')
    with open('scores/score_test.txt', 'r') as test:
        for _ in range(10):
            line = test.readline().strip('\n')
            assert line == 'DFT 0'

        test.close()
