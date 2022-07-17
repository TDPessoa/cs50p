"""In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

convert
    expects a str in X/Y format as input,
        wherein each of X and Y is an integer,
        and returns that fraction as a percentage
            rounded to the nearest int between 0 and 100, inclusive.
        If X and/or Y is not an integer,
        or if X is greater than Y,
            then convert should raise a ValueError.
        If Y is 0,
            then convert should raise a ZeroDivisionError.

gauge
    expects an int and returns a str that is:
        "E" if that int is less than or equal to 1,
        "F" if that int is greater than or equal to 99,
        and "Z%" otherwise, wherein Z is that same int.

<code>
def main():
    ...


def convert(fraction):
    ...


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()
</code>

Then, in a file called test_fuel.py, implement two or more functions that collectively test your implementations of
convert and gauge thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

<pytest test_fuel.py>"""

import pytest
from fuel import convert, gauge


# Receives an <str> formatted as X/Y and outputs a value(0,100)
def test_convert():
    assert convert('1/2') == 50
    assert convert('1/100') == 1
    assert convert('3/4') == 75
    # Rounding values
    assert convert('1/1000') == 0
    assert convert('199/200') == 100


# Errors:
def test_convert_exceptions():
    # Won't accept an X value greater then the Y value
    with pytest.raises(ValueError):
        convert('2/1')
    # Won't accept an Y value of 0
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
    # Won't accept values that can't be transformed into integers
    with pytest.raises(ValueError):
        convert('F/3')


# Returns an <str> per parameter(value) where:
def test_gauge_empty():
    # value <= 1: returns 'E'
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'


# 1 < value < 99: returns f'{value:.0f}%'
def test_gauge_middle():
    assert gauge(50) == '50%'


def test_gauge_full():
    # value <= 99: returns 'F'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'


"""This was the output of the build-in 'check50' function"""
# :) test_fuel.py exist
# :) correct fuel.py passes all test_fuel checks
# :) test_fuel catches fuel.py returning incorrect ints in convert
# :) test_fuel catches fuel.py not raising ValueError in convert
# :) test_fuel catches fuel.py not raising ZeroDivisionError in convert
# :) test_fuel catches fuel.py not labeling 1% as E in gauge
# :) test_fuel catches fuel.py not printing % in gauge
# :) test_fuel catches fuel.py not labeling 99% as F in gauge
