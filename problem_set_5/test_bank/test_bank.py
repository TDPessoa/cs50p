"""In a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the
below, wherein value expects a str as input and returns 0 if that str starts with “hello”, 20 if that str starts with
an “h” (but not “hello”), or 100 otherwise, treating the str case-insensitively. Only main should call print.

<code>
def main():
    ...


def value(greeting):
    ...


if __name__ == "__main__":
    main()
</code>

Then, in a file called test_bank.py, implement three or more functions that collectively test your implementation of
value thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

<pytest test_bank.py>"""

from bank import value


def test_value_hello():
    assert value('hello, thiago') == 0
    assert value('hello, d-a-v-i-d') == 0
    assert value('hello, Kramer') == 0


def test_value_h():
    assert value('h') == 20
    assert value('how you doin?') == 20
    assert value('hey, CS50') == 20


def test_value_no_h():
    assert value('one, two, tree') == 100
    assert value('this is a phrase') == 100
    assert value("I'm coding") == 100


def test_value_upper():
    assert value('HELLO') == 0
    assert value('HEY') == 20
    assert value('ONE') == 100
