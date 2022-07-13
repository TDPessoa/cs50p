"""In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names when those
names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each
subsequent word is uppercase. For instance, whereas a variable for a user’s name might be called name, a variable for a
user’s first name might be called firstName, and a variable for a user’s preferred first name (e.g., nickname) might
be called preferredFirstName.

Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters
in lowercase. For instance, those same variables would be called name, first_name, and preferred_first_name,
respectively, in Python.

In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and
outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case."""


def main():
    final_name = ''
    name_var = str(input("Whats the name of the variable?"))
    for c in name_var:
        if checker(c) and not name_var[0] == c:
            final_name += '_' + c.lower()
        else:
            final_name += c
    print(final_name)


def checker(letter):
    if letter == letter.upper():
        return True
    else:
        return False


if __name__ == '__main__':
    main()

"""This was the output of the build-in 'check50' function"""
# :) camel.py exists
# :) input of "name" yields output of "name"
# :) input of "firstName" yields output of "first_name"
# :) input of "preferredFirstName" yields output of "preferred_first_name"
