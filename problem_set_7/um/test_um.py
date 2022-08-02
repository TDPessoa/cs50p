from um import count


def test_count_zeros():
    assert count('') == 0
    assert count('umum') == 0
    assert count('This is umCS50') == 0


def test_count_ones():
    assert count('um') == 1
    assert count('um mum') == 1
    assert count('This is, um, CS50.') == 1


def test_count_twos():
    assert count('um um') == 2
    assert count('um um mum') == 2
    assert count('This, um, is, um, CS50!') == 2


def test_count_upper():
    assert count('Um um') == 2
    assert count('Um Um') == 2
    assert count('um Um') == 2
    assert count('UM Um') == 2
    assert count('Um UM') == 2
    assert count('UM UM') == 2


"""This was the output of the build-in 'check50' function"""
# :) um.py and test_um.py exist
# :) um.py yields 1 for "um"
# :) um.py yields 1 for "Hello, um, world"
# :) um.py yields 1 for "This is, um... CS50."
# :) um.py yields 1 for "Um... what are regular expressions?"
# :) um.py yields 2 for "Um, thanks, um, regular expressions make sense now."
# :) um.py yields 2 for "Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?"
# :) correct um.py passes all test_um.py checks
# :) test_um.py catches um.py matching "um" in words
# :) test_um.py catches um.py with regular expression requiring spaces around "um"
# :) test_um.py catches um.py without case-insensitive matching of "um"
