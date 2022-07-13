"""WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same
input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to
prompt the user explicitly, as by passing a str of your own as an argument to input."""


def ___main___():
    phrase = str(input('\nPlease, speak quietly.\nWhat would you like to say?'))
    print(phrase.lower(), '\n')


___main___()

"""This was the output of the build-in 'check50' function"""
# :) indoor.py exists
# :) input of HELLO yields output of hello
# :) input of THIS IS CS50 yields output of this is cs50
# :) input of 50 yields output of 50
