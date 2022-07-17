"""This file will be tested by <test_plates.py> file"""


# Declaring useful CONSTANTS
LETTERS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')


def main():
    plate = input('Plate:')
    if is_valid(plate):
        print('Valid')

    else:
        print('Invalid')


# Main Verifier
def is_valid(plate):
    if length_checker(plate) and two_first_checker(plate) and no_first_zero(plate) and \
       lasts_are_number_checker(plate) and no_special_chars(plate):
        return True

    else:
        return False


# Minor Verifier n1. The first two characters have to be letters.
def two_first_checker(plate):
    if (plate[0] in LETTERS) and (plate[1] in LETTERS):
        return True

    else:
        return False


# Minor Verifier n2. The plate has to have a minimum of 2 and a maximum of 6 characters.
def length_checker(plate):
    if 2 <= len(plate) <= 6:
        return True

    else:
        return False


# Minor Verifier n3. The numbers can't be in the middle of the plate.
def lasts_are_number_checker(plate):
    for c in range(len(plate)):
        if plate[c] in LETTERS:
            for i in range(c):
                if plate[i] in NUMBERS:
                    return False

                else:
                    pass

        else:
            pass
    return True


# Minor Verifier n4. No special characters.
def no_special_chars(plate):
    for c in plate:
        if (c.upper() in LETTERS) or (c in NUMBERS):
            pass

        else:
            return False
    return True


# Minor Verifier n5. No zero as first number.
def no_first_zero(plate):
    num_count = 0
    for c in plate:
        if (c in NUMBERS) and \
                (c != '0'):
            num_count += 1

        elif num_count != 0:
            break

        elif c == '0':
            return False

        else:
            pass
    return True


if __name__ == '__main__':
    main()
