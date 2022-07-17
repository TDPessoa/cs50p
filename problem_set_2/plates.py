"""In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with
your choice of letters and numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable
 … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the
requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your
 program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume
 that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per
 requirement).

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...


main()"""

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
    if (len(plate) >= 2) and (len(plate) <= 6):
        return True

    else:
        return False


# Minor Verifier n3. The numbers can't be in the middle of the plate.
def lasts_are_number_checker(plate):
    print('Entering in verifier n3')
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


main()

"""This was the output of the build-in 'check50' function"""
# :) plates.py exists
# :) input of CS50 yields output of Valid
# :) input of ECTO88 yields output of Valid
# :) input of NRVOUS yields output of Valid
# :) input of CS05 yields output of Invalid
# :) input of CS50P2 yields output of Invalid
# :) input of PI3.14 yields output of Invalid
# :) input of H yields output of Invalid
# :) input of OUTATIME yields output of Invalid
