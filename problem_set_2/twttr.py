"""When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like
 Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of
 text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or
 lowercase."""


def main():
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    phrase = str(input("What would you like to say?"))
    final_phrase = ''
    for c in phrase:
        if c.lower() not in vowel_list:
            final_phrase += c

    print(final_phrase)


if __name__ == '__main__':
    main()

"""This was the output of the build-in 'check50' function"""
# :) twttr.py exists
# :) input of Twitter yields output of Twttr
# :) input of "What's your name?" yields output of "Wht's yr nm?"
# :) input of CS50 yields output of CS50
# :) input of PYTHON yields output of PYTHN
