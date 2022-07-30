from working import convert
import pytest


def test_with_minutes():
    assert convert('1:00 AM to 1:00 PM') == '01:00 to 13:00'
    assert convert('1:00 PM to 1:00 AM') == '13:00 to 01:00'
    assert convert('1:15 AM to 1:00 PM') == '01:15 to 13:00'
    assert convert('1:45 AM to 1:00 PM') == '01:45 to 13:00'


def test_without_minutes():
    assert convert('1 AM to 1 PM') == '01:00 to 13:00'
    assert convert('1 PM to 1 AM') == '13:00 to 01:00'


def test_errors():
    # Hours out of range:
    with pytest.raises(ValueError):
        convert('13 AM to 1 PM')
    with pytest.raises(ValueError):
        convert('100 AM to 1 PM')
    with pytest.raises(ValueError):
        convert('1 AM to 13 PM')
    with pytest.raises(ValueError):
        convert('1 AM to 100 PM')
    with pytest.raises(ValueError):
        convert('13:00 AM to 01:00 PM')
    with pytest.raises(ValueError):
        convert('100:00 AM to 01:00 PM')
    with pytest.raises(ValueError):
        convert('01:00 AM to 13:00 PM')
    with pytest.raises(ValueError):
        convert('01:00 AM to 100:00 PM')

    # Minutes out of range:
    with pytest.raises(ValueError):
        convert('1:00 AM to 1:75 PM')
    with pytest.raises(ValueError):
        convert('1:75 AM to 1:00 PM')

    # Syntax error:
    with pytest.raises(ValueError):
        convert('1:00AM to 1:00AM')
    with pytest.raises(ValueError):
        convert('1:00 to 1:75 PM')
    with pytest.raises(ValueError):
        convert('1:00 AM to 1:75')
    with pytest.raises(ValueError):
        convert('01:00 to 13:00')
    with pytest.raises(ValueError):
        convert('cat')
    with pytest.raises(ValueError):
        convert('1:00 AM 1:00 PM')


"""This was the output of the build-in 'check50' function"""
# :) working.py and test_working.py exist
# :) working.py does not import libraries other than sys and re
# :) working.py converts "9 AM to 5 PM" to "09:00 to 17:00"
# :) working.py converts "9:00 AM to 5:00 PM" to "09:00 to 17:00"
# :) working.py converts "8 PM to 8 AM" to "20:00 to 08:00"
# :) working.py converts "8:00 PM to 8:00 AM" to "20:00 to 08:00"
# :) working.py converts "12 AM to 12 PM" to "00:00 to 12:00"
# :) working.py converts "12:00 AM to 12:00 PM" to "00:00 to 12:00"
# :) working.py raises ValueError when given "8:60 AM to 4:60 PM"
# :) working.py raises ValueError when given "9AM to 5PM"
# :) working.py raises ValueError when given "09:00 to 17:00"
# :) working.py raises ValueError when given "9 AM - 5 PM"
# :) working.py raises ValueError when given "10:7 AM - 5:1 PM"
# :) correct working.py passes all test_working checks
# :) test_working.py catches working.py printing incorrect hours
# :) test_working.py catches working.py printing incorrect minutes
# :) test_working.py catches working.py not raising ValueError when user omits " to "
# :) test_working.py catches working.py not raising ValueError for out-of-range times
# :) test_working.py catches working.py not raising ValueError for invalid time format
