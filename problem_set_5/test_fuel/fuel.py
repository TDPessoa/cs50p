"""This file will be tested by the <test_fuel.py> file"""


def main():
    while True:
        try:
            entry = str(input("What's the fraction?"))
            print(gauge(convert(entry)))
            break

        except ZeroDivisionError:
            pass

        except ValueError:
            pass


def convert(fraction):
    fraction = fraction.split('/')
    if int(fraction[0]) < int(fraction[1]):
        value = int(fraction[0]) / int(fraction[1]) * 100
        return int(round(value))
    elif int(fraction[1]) == 0:
        raise ZeroDivisionError

    else:
        raise ValueError


def gauge(num):
    if 0 <= num <= 1:
        return 'E'

    elif 1 < num < 99:
        return f'{num:.0f}%'

    elif 99 <= num <= 100:
        return 'F'

    else:
        raise ValueError


if __name__ == '__main__':
    main()
