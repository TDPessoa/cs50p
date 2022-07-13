"""In a file called bitcoin.py, implement a program that:
    Expects the user to specify as a command-line argument the number of Bitcoins, , that they would like to buy. If
that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
    Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which
returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any
exceptions, as with code like:

        import requests

        try:
            ...
        except requests.RequestException:
            ...

Outputs the current cost of  Bitcoins in USD to four decimal places, using , as a thousands separator."""

import sys, requests


def main():
    try:
        x = float(sys.argv[1])
    except IndexError:
        sys.exit('Command-line is not a number')
    except ValueError:
        sys.exit("Missing command-line argument")

    coindesk = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    coindesk_text = coindesk.text

    coindesk_text = coindesk_text.replace('{', ',').replace('}', ",").replace(':', ',')
    coindesk_text = coindesk_text.split(',')

    for c in range(len(coindesk_text)):
        try:
            if coindesk_text[c] == '"rate_float"':
                num = float(coindesk_text[c + 1])
                print(f'${x * num:,.4f}')
                exit()
        except ValueError:
            pass


main()

'''Although the code is very "brittle" and bad structured...'''
"""This was the output of the build-in 'check50' function"""
# :) bitcoin.py exists
# :) bitcoin.py exits given no command-line argument
# :) bitcoin.py exits given non-numeric command-line argument
# :) bitcoin.py provides price of 1 Bitcoin to 4 decimal places
# :) bitcoin.py provides price of 2 Bitcoin to 4 decimal places
# :) bitcoin.py provides price of 2.5 Bitcoin to 4 decimal places
"""After some more experience, I'm going to come back to it and rebuilding."""
