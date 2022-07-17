## Just a disclaimer:

I wrote a much bigger test_file for this problem_set, trying to catch errors in __every function__ that I implemented in the original file.

After I was finished and started running the pytests I got a weird error saying that there was an `AtributeError` in which the `length_checker()` wasn't found in the plates.py file. 

After this happened it hit me just as last night as I was doing the last test_file, I can't submit to CS50 like this because they have their own files to be tested and the syntax will be different then mine. So I re-wrote as the file is in branch master.

Although I completed and submitted, I still don't understand what caused the error. Some day in the future, if I have the answer, I'll put it in here.

Here it's the original test_file I intended to make: 

```
import plates


\# Is True if all bellow return True.
def test_is_valid():
    assert plates.is_valid('CS50') is True
    assert plates.is_valid('CS05') is False
    assert plates.is_valid('VANITY') is True
    assert plates.is_valid('C50S') is False
    assert plates.is_valid('Th1ago') is False


\# Is True if the first two characters are letters.
def test_two_first_checker():
    assert plates.two_first_checker('CS50') is True
    assert plates.two_first_checker('50CS') is False
    assert plates.two_first_checker('C50S') is False
    assert plates.two_first_checker('CS..') is True
    assert plates.two_first_checker('VAn1ty') is True


\# Is True if the length of the <str> is from 2 to 6 characters long.
def test_length_checker():
    assert plates.length_checker('1) is True
    assert plates.lenght_checker('12') is True
    assert plates.lenght_checker('123') is True
    assert plates.lenght_checker('1234') is True
    assert plates.lenght_checker('12345') is True
    assert plates.lenght_checker('123456') is True
    assert plates.lenght_checker('1234567') is False


\# Is True if there are no numbers before a letter in the <str>.
def test_lasts_are_number_checker():
    assert plates.lasts_are_number_checker('CS50') is True
    assert plates.lasts_are_number_checker('C50S') is False
    assert plates.lasts_are_number_checker('1') is True
    assert plates.lasts_are_number_checker('TTHHIIGGOO50') is True
    assert plates.lasts_are_number_checker('THIAGO') is True


\# Is True if all characters are letters or numbers, no specials.
def test_no_special_chars():
    assert plates.no_special_chars('1') is True
    assert plates.no_special_chars('!') is False
    assert plates.no_special_chars('ABCDE') is True
    assert plates.no_special_chars('12345') is True
    assert plates.no_special_chars('A') is True
    assert plates.no_special_chars('!@#$%') is False


\# Is True if the first number to appear isn't a zero.
def test_no_first_zero():
    assert plates.no_first_zero('1') is True
    assert plates.no_first_zero('0') is False
    assert plates.no_first_zero('123') is True
    assert plates.no_first_zero('CSS01') is False
    assert plates.no_first_zero('CS05P') is False
    assert plates.no_first_zero('CS50P') is True
```