"""In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the
below, wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U)
omitted, whether inputted in uppercase or lowercase.

def main():
    ...


def shorten(word):
    ...


if __name__ == "__main__":
    main()
Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of
shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests with:"""


from twttr import shorten


def test_shorten():
    assert shorten('testing') == 'tstng'
    assert shorten('shorten') == 'shrtn'
    assert shorten('cs50') == 'cs50'
    assert shorten('TESTING') == 'TSTNG'
    assert shorten('this, is a line.') == 'ths, s  ln.'


"""This was the output of the build-in 'check50' function"""
# :) test_twttr.py exist
# :) correct twttr.py passes all test_twttr checks
# :) test_twttr catches twttr.py without vowel replacement
# :) test_twttr catches twttr.py without capitalized vowel replacement
# :) test_twttr catches twttr.py without lowercase vowel replacement
# :) test_twttr catches twttr.py omitting numbers
# :) test_twttr catches twttr.py printing in uppercase
# :) test_twttr catches twttr.py omitting punctuation
