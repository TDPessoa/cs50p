"""Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( was a sad face.
Nowadays, programs tend to convert emoticons to emoji automatically!

In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input
with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as
 a slightly frowning face). All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input,
and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your
own as an argument to input. Be sure to call main at the bottom of your file."""


def main():
    phrase = str(input("\nWhat would you like to say?"))
    print(convert(phrase))


def convert(phr):
    phr = phr.replace(':)', '🙂')
    phr = phr.replace(':(', '🙁')
    return phr


main()

"""This was the output of the build-in 'check50' function"""
# :) faces.py exists
# :) input of "Hello :)" yields output of "Hello 🙂"
# :) input of "Goodbye :(" yields output of "Goodbye 🙁"
# :) input of "Hello :) Goodbye :(" yields output of "Hello 🙂 Goodbye 🙁"
