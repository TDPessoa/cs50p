"""Assuming there are 365 days in a year, there are  minutes in that same year (because there are 24 hours in a day and
60 minutes in an hour). But how many minutes are there in two or more years? Well, it depends on how many of those are
leap years with 366 days, per the Gregorian calendar, as some of them could have  additional minutes. In fact, how many
minutes has it been since you were born? Well, that, too, depends on how many leap years there have been since! There
is an algorithm for such, but let’s not reinvent that wheel. Let’s use a library instead. Fortunately, Python comes
with a datetime module that has a class called date that can help,
per docs.python.org/3/library/datetime.html#date-objects.

In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD format and
then sings prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals,
just like the song from Rent, without any and between words. Since a user might not know the time at which they were
born, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the
current time is also midnight. In other words, even if the user runs the program at noon, assume that it’s actually
midnight, on the same date. Use datetime.date.today to get today’s date,
per docs.python.org/3/library/datetime.html#datetime.date.today.

Structure your program per the below, not only with a main function but also with one or more other functions as well:

    from datetime import date


    def main():
        ...


    ...


    if __name__ == "__main__":
        main()

You’re welcome to import other (built-in) libraries. Exit via sys.exit if the user does not input a date in YYYY-MM-DD
format. Ensure that your program will not raise any exceptions.

Either before or after you implement seasons.py, additionally implement, in a file called test_seasons.py, one or more
functions that test your implementation of any functions besides main in seasons.py thoroughly, each of whose names
should begin with test_ so that you can execute your tests with:

pytest test_seasons.py"""

from datetime import date
import inflect


def main():
    try:
        # Getting the input
        birthday = str(input('Enter with your date as YYYY-MM-DD:'))
        print(sing(birthday))

    except ValueError:
        exit('ValueError')

    except IndexError:
        exit("IndexError")


def sing(birthday):
    # Starting inflect
    p = inflect.engine()

    # Setting values for time()
    year = int(birthday.split('-')[0])
    month = int(birthday.split('-')[1])
    day = int(birthday.split('-')[2])

    # Subtracting the inputted date from the current date
    elapsed = str(date.today() - date(year, month, day)).split(' ')

    # Multiplying the number of days in elapsed by 'hours in day'(24) and 'minutes in hour'(60)
    minutes = int(elapsed[0]) * 60 * 24

    # Formatting, using inflect, the count of minutes
    words = p.number_to_words(minutes, andword="")
    return f'{words} minutes'.capitalize()


if __name__ == "__main__":
    main()

"""This was the output of the build-in 'check50' function"""
# :) seasons.py and test_seasons.py exist
# :) Input of "1999-01-01" yields "Five hundred twenty-five thousand, six hundred minutes" when today is 2000-01-01
# :) Input of "2001-01-01" yields "One million, fifty-one thousand, two hundred minutes" when today is 2003-01-01
# :) Input of "1995-01-01" yields "Two million, six hundred twenty-nine thousand, four hundred forty minutes" when
# today is 2000-01-1
# :) Input of "2020-06-01" yields "Six million, ninety-two thousand, six hundred forty minutes" when today is 2032-01-01
# :) Input of "1998-06-20" yields "Eight hundred six thousand, four hundred minutes" when today is 2000-01-01
# :) Input of "February 6th, 1998" prompts program to exit with sys.exit
# :) seasons.py passes all checks in test_seasons.py