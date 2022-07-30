"""In a file called working.py, implement a function called convert that expects a str in either of
the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00).
Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space
before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and
5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
Raise a ValueError instead if the input to convert is not in either of those formats or if either
time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start
ante meridiem and end post meridiem; someone might work late and even long hours
(e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main and/or implement other
functions as you see fit, but you may not import any other libraries. You’re welcome, but not
required, to use re and/or sys."""

from re import search


def main():
    print(convert(input('Time?')))


def convert(hours):
    if search(r'^\d{1,2}:\d{2} (AM|PM) to \d{1,2}:\d{2} (AM|PM)$', hours):
        # 5:00 PM to 9:00 AM >> 5 00 PM to 9 00 AM >> ['5', '00', 'PM', 'to', '9', '00', 'AM']
        checker = hours.replace(':', ' ').split(' ')
        times = [checker[2], checker[6]]
        checker = [int(checker[0]), int(checker[1]), int(checker[4]), int(checker[5])]
        if 0 <= checker[0] <= 12 and \
                0 <= checker[1] < 60 and \
                0 <= checker[2] <= 12 and \
                0 <= checker[3] < 60:

            if checker[0] == checker[2] == 12:
                checker[0], checker[2] = 0, 0

            elif checker[0] == 12:
                checker[0] = 0

            elif checker[2] == 12:
                checker[2] = 0

            if times[0] == 'PM':
                checker[0] += 12

            if times[1] == 'PM':
                checker[2] += 12

            return f'{checker[0]:0>2}:{checker[1]:0>2} to {checker[2]:0>2}:{checker[3]:0>2}'

        else:
            raise ValueError

    elif search(r'^\d{1,2} (AM|PM) to \d{1,2} (AM|PM)$', hours):
        # 5 PM to 9 AM >> 5 PM to 9 AM >> ['5', 'PM', 'to', '9', 'AM']
        checker = hours.split(' ')
        times = [checker[1], checker[4]]
        checker = [int(checker[0]), int(checker[3])]
        if 0 <= checker[0] <= 12 and \
                0 <= checker[1] <= 12:
            if checker[0] == checker[1] == 12:
                checker[0], checker[1] = 0, 0

            elif checker[0] == 12:
                checker[0] = 0

            elif checker[1] == 12:
                checker[1] = 0

            if times[0] == 'PM':
                checker[0] += 12

            if times[1] == 'PM':
                checker[1] += 12

            return f'{checker[0]:0>2}:00 to {checker[1]:0>2}:00'

        else:
            raise ValueError

    else:
        raise ValueError


if __name__ == '__main__':
    main()


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
