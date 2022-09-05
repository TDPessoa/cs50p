"""Suppose that you’d like to implement a cookie jar in which to store cookies. In a file called jar.py, implement a
class called Jar with these methods:

    __init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies
that can fit in the cookie jar. If capacity is not a non-negative int, though,
__init__ should instead raise a ValueError.
    __str__ should return a str with  🍪, where  is the number of cookies in the cookie jar. For instance,
if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
    deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity,
though, deposit should instead raise a ValueError.
    withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the
cookie jar, though, withdraw should instead raise a ValueError.
    capacity should return the cookie jar’s capacity.
    size should return the number of cookies actually in the cookie jar.

Structure your class per the below. You may not alter these methods’ parameters, but you may add your own methods.

class Jar:
    def __init__(self, capacity=12):
        ...

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...


Either before or after you implement jar.py, additionally implement, in a file called test_jar.py, four or more
functions that collectively test your implementation of Jar thoroughly, each of whose names should begin with test_
so that you can execute your tests with:

pytest test_jar.py
Note that it’s not as easy to test instance methods as it is to test functions alone, since instance methods sometimes
manipulate the same “state” (i.e., instance variables). To test one method (e.g., withdraw), then, you might need to
call another method first (e.g., deposit). But the method you call first might itself not be correct!

And so programmers sometimes mock (i.e., simulate) state when testing methods, as with Python’s own mock object
library, so that you can call just the one method but modify the underlying state first, without calling the other
method to do so.

For simplicity, though, no need to mock any state. Implement your tests as you normally would!"""


class Jar:
    # __init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies
    # that can fit in the cookie jar. If capacity is not a non-negative int, though,
    # __init__ should instead raise a ValueError.
    def __init__(self, capacity=12):
        self.capacit = capacity
        if self.capacit < 0:
            raise ValueError
        self.cookies = 0

    # __str__ should return a str with  🍪, where  is the number of cookies in the cookie jar. For instance,
    # if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
    def __str__(self):
        return self.cookies * "🍪"

    # deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity,
    # though, deposit should instead raise a ValueError.
    def deposit(self, n):
        self.cookies += n
        if self.cookies > self.capacit:
            raise ValueError

    # withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the
    # cookie jar, though, withdraw should instead raise a ValueError.
    def withdraw(self, n):
        self.cookies -= n
        if self.cookies < 0:
            raise ValueError

    # capacity should return the cookie jar’s capacity.
    @property
    def capacity(self):
        return self.capacit

    # size should return the number of cookies actually in the cookie jar.
    @property
    def size(self):
        return self.cookies


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
