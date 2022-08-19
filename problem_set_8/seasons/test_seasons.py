"""This code will be used to test the seasons.py file"""
from seasons import sing
from pytest import raises


def test_correct():
    assert sing("1999-01-01") == "Twelve million, four hundred twenty-eight thousand, six hundred forty minutes"
    assert sing("2001-01-01") == "Eleven million, three hundred seventy-six thousand minutes"
    assert sing("1995-01-01") == "Fourteen million, five hundred thirty-two thousand, four hundred eighty minutes"
    assert sing("2020-06-01") == "One million, one hundred sixty-four thousand, nine hundred sixty minutes"
    assert sing("1998-06-20") == "Twelve million, seven hundred nine thousand, four hundred forty minutes"

def test_errors():
    with raises(Exception):
        sing("February 6th, 1998")
    with raises(Exception):
        sing('asd')
    with raises(Exception):
        sing(1)