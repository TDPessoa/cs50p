"""In a file called response.py, using either <validator-collection> or <validators> from PyPI,
    implement a program that:
        prompts the user for an email address via input and then
        prints Valid or Invalid,
            respectively, if the input is a syntatically valid email address.

    You may not use re.
    And do not validate whether the email address’s domain name actually exists."""


from validator_collection import is_email

def main():
    if is_email(str(input("What's your e-mail adress?"))):
        print("Valid")
    else:
        print("Invalid")


if __name__ == '__main__':
    main()

"""This was the output of the build-in 'check50' function"""
# :) response.py exists
# :) response.py does not use re and uses either validators or validator-collection
# :) response.py yields Valid when email address is "malan@harvard.edu"
# :) response.py yields Valid when email address is "sysadmins@cs50.harvard.edu"
# :) response.py yields Invalid when email address is "malan at harvard dot edu"
# :) response.py yields Invalid when email address is "malan@@@harvard.edu"
