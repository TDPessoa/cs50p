"""Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank
is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X
and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more
remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not
necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError."""


def main():
    while True:
        entry = str(input("What's the fraction?"))
        try:
            entry = entry.split('/')
            if int(entry[0]) <= int(entry[1]):
                value = int(entry[0]) / int(entry[1]) * 100
                break
            else:
                pass

        except BaseException:
            pass

    if value <= 1:
        print('E')

    elif 1 < value < 99:
        print(f'{int(round(value, 0))}%')

    elif value >= 99:
        print('F')


main()
