"""In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below,
wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does
not, but main is only called if the value of __name__ is "__main__":

<code>
def main():
    ...


def is_valid(s):
    ...


if __name__ == "__main__":
    main()
</code>

Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of
is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

<pytest test_plates.py>"""

from plates import is_valid


# Is True if all bellow return True.
def test_is_valid():
    assert is_valid('CS50') is True
    assert is_valid('CS05') is False
    assert is_valid('VANITY') is True
    assert is_valid('C50S') is False
    assert is_valid('Th1ago') is False
    assert is_valid('50') is False
    assert is_valid('A') is False
    assert is_valid('ABCDEFG') is False
    assert is_valid('AB!@') is False


"""This was the output of the build-in 'check50' function"""
# :) test_plates.py exist
# :) correct plates.py passes all test_plates checks
# :) test_plates catches plates.py without beginning alphabetical checks
# :) test_plates catches plates.py without length checks
# :) test_plates catches plates.py without checks for number placement
# :) test_plates catches plates.py without checks for zero placement
# :) test_plates catches plates.py without checks for alphanumeric characters
