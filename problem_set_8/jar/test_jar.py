"""This code will test the class in jar.py"""

from jar import Jar
from pytest import raises

# Open your test_jar.py file and import your Jar class with from jar import Jar. Create a function called test_init,
# wherein you create a new instance of Jar with jar = Jar(). assert that this jar has the capacity it should, then
# run your tests with pytest test_jar.py.


def test_init():
    jar = Jar()
    assert jar.capacity == 12

# Add another function to your test_jar.py file called test_str. In test_str, create a new instance of your Jar class
# and deposit a few cookies. assert that str(jar) prints out as many cookies as have been deposited, then run your
# tests with pytest test_jar.py.


def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"

# Add another function to your test_jar.py file called test_deposit. In test_deposit, create a new instance of your
# Jar class and deposit a few cookies. assert that the jar’s size attribute is as large as the number of cookies that
# have been deposited. Also assert that, if you deposit more than the jar’s capacity, deposit should raise a
# ValueError. Run your tests with pytest test_jar.py.


def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(3)
    assert jar.size == 6
    with raises(ValueError):
        jar.deposit(7)

# Add another function to your test_jar.py file called test_withdraw. In test_withdraw, create a new instance of
# your Jar class and first deposit a few cookies. assert that withdrawing from the jar leaves the appropriate
# number of cookies in the jar’s size attribute. Also assert that, if you withdraw more than the jar’s size,
# withdraw should raise a ValueError. Run your tests with pytest test_jar.py.


def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(4)
    assert str(jar) == "🍪🍪🍪🍪"
    with raises(ValueError):
        jar.withdraw(5)


"""This was the output of the build-in 'check50' function"""
# :) jars.py exists
# :) Jar's constructor initializes a cookie jar with given capacity
# :) Jar's constructor raises ValueError when called with negative capacity
# :) Empty jar prints zero cookies
# :) Jar prints total number of cookies deposited
# :) Jar's deposit method raises ValueError when deposited cookies exceed the jar's capacity
# :) Jar's withdraw method removes cookies from the jar's size
# :) Jar's withdraw method raises ValueError when withdrawn cookies exceed jar's size
# :) Implementation of Jar passes all tests in test_jar.py
# :) test_jar.py contains at least four functions
