"""Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these
denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time
informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the
user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted
denomination."""


# The machine accepts 5¢, 10¢, 25¢ and 50¢*
# The machine will not prompt the user for the input, but the 'Due Value'.

def main():
    value = 0
    while value < 50:
        print('Due Value:', value)
        cents = int(input())
        if cents == 5 or \
                cents == 10 or \
                cents == 25 or \
                cents == 50:
            value += cents
    value -= 50
    print('Change owned:', value)


main()

"""This was the output of the build-in 'check50' function"""
# :) coke.py exists
# :) coke accepts 25 cents
# :) coke accepts 10 cents
# :) coke accepts 5 cents
# :) coke rejects invalid amount of cents
# :) coke accepts continued input
# :) coke terminates at 50 cents
# :) coke provides correct change
