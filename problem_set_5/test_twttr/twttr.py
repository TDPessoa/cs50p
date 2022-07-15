"""This file will be tested by the <test_twttr.py> file"""


def main():
    phrase = str(input("What would you like to say?"))
    print(shorten(phrase))


def shorten(phrase):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    final_phrase = ''
    for c in phrase:
        if c.lower() not in vowel_list:
            final_phrase += c

    return final_phrase


if __name__ == '__main__':
    main()
