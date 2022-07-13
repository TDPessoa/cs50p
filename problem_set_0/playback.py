"""Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s
0.75 playback speed, or even by having them pause between words.

In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same
input, replacing each space with ... (i.e., three periods)."""


def main():
    phrase = str(input('\nWhat would you like to say?'))
    print(phrase.replace(' ', '...'))


main()

"""This was the output of the build-in 'check50' function"""
# :) playback.py exists
# :) input of "This is CS50" yields output of "This...is...CS50"
# :) input of "This is our week on functions" yields output of "This...is...our...week...on...functions"
# :) input of "Let's implement a function called hello" yields output of \
#    "Let's...implement...a...function...called...hello"
