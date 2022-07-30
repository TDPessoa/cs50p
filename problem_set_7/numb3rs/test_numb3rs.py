"""Code to test the <validade> function in the numb3rs.py file"""

from numb3rs import validate


def test_syntax():
    assert validate('123.123.123.123') is True
    assert validate('123.123.123') is False
    assert validate('cat') is False
    assert validate('1.1.1.1') is True


def test_cell_range():
    assert validate('1.1.1.1') is True
    assert validate('255.255.255.255') is True
    assert validate('0.0.0.0') is True
    assert validate('256.256.255.255') is False
    assert validate('1000.1000.1000.1000') is False


def test_by_bytes():
    assert validate('1.300.300.300') is False
    assert validate('300.1.300.300') is False
    assert validate('300.300.1.300') is False
    assert validate('300.300.300.1') is False


"""This was the output of the build-in 'check50' function"""
# :) numb3rs.py exists
# :) numb3rs.py prints True for 127.0.0.1
# :) numb3rs.py prints True for 255.255.255.255
# :) numb3rs.py prints True for 140.247.235.144
# :) numb3rs.py prints False for 256.255.255.255
# :) numb3rs.py prints False for 64.128.256.512
# :) numb3rs.py prints False for 2001:0db8:85a3:0000:0000:8a2e:0370:7334
# :) numb3rs.py prints False for cat
# :) correct numb3rs.py passes all test_numb3rs.py checks
# :) test_numb3rs.py catches numb3rs.py only checking first byte of IPv4 address
# :) test_numb3rs.py catches numb3rs.py failing to return False for invalid IPv4 format
