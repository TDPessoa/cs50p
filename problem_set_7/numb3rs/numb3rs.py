"""In Season 5, Episode 23 of NUMB3RS, a supposed IP address appears on screen, 275.3.6.28, which
isn’t actually a valid IPv4 (or IPv6) address.

An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on
the internet, akin to a postal address in the real world, typically formatted in dot-decimal
notation as #.#.#.#. But each # should be a number between 0 and 255, inclusive. Suffice it to
say 275 is not in that range! If only NUMB3RS had validated the address in that scene!

In a file called numb3rs.py, implement a function called validate that expects an IPv4 address
as input as a str and then returns True or False, respectively, if that input is a valid IPv4
address or not.

Structure numb3rs.py as follows, wherein you’re welcome to modify main and/or implement other
functions as you see fit, but you may not import any other libraries. You’re welcome, but not
required, to use re and/or sys.


    import re
    import sys


    def main():
        print(validate(input("IPv4 Address: ")))


    def validate(ip):
        ...


    ...


    if __name__ == "__main__":
        main()


Either before or after you implement validate in numb3rs.py, additionally implement, in a file
called test_numb3rs.py, two or more functions that collectively test your implementation of
validate thoroughly, each of whose names should begin with test_ so that you can execute your
tests with:"""

from re import search


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if search(r'^\d+\.\d+\.\d+\.\d+$', ip) and range_check(ip):
        return True
    else:
        return False


def range_check(string):
    for n in string.split('.'):
        if 0 <= int(n) <= 255:
            pass

        else:
            return False

    return True


if __name__ == "__main__":
    main()


"""This was the output of the build-in 'check50' function"""
# :) numb3rs.py exists
# :) numb3rs.py prints True for 127.0.0.1
# :) numb3rs.py prints True for 255.255.255.255
# :) numb3rs.py prints True for 140.247.235.144
# :) numb3rs.py prints False for 256.255.255.255
# :) numb3rs.py prints False for 64.128.256.512
# :) numb3rs.py prints False for 2001:0db8:85a3:0000:0000:8a2e:0370:7334
# :) numb3rs.py prints False for cat
# :) correct numb3rs.py passes all test_numb3rs.py checks
# :) test_numb3rs.py catches numb3rs.py only checking first byte of IPv4 address
# :) test_numb3rs.py catches numb3rs.py failing to return False for invalid IPv4 format
