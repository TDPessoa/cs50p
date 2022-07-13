"""In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs
control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with
one and, three names with two commas and one and, and  names with  commas and one and, as in the below:
Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl"""


'''The problem_set, found in the url: https://cs50.harvard.edu/python/2022/psets/4/adieu/, specify that it must be 
used a library called <inflect> but, the check50 function accepted the code bellow with "green smilies" as well.'''

# def without_imports():
#     list_of_names = []
#     try:
#         while True:
#             name = str(input('Name:'))
#             list_of_names.append(name)
#     except EOFError:
#         for n in range(len(list_of_names)):
#             if n == 0:
#                 print(f'Adieu, adieu, to {list_of_names[0]}', end='')
#             elif n == len(list_of_names) - 1:
#                 if len(list_of_names) > 2:
#                     print(f', and {list_of_names[-1]},', end='')
#                 else:
#                     print(f' and {list_of_names[-1]}', end='')
#             else:
#                 print(f', {list_of_names[n]}', end='')
#
#
# without_imports()

# >>> I know that it's a longer code and I'm "re-inventing the wheel", but I wanted to do it. :)
'''Now, to the actual code'''


import inflect


def main():
    p = inflect.engine()
    list_of_names = []
    try:
        while True:
            name = str(input('Name:'))
            list_of_names.append(name)
    except EOFError:
        print(f'Adieu, adieu, to {p.join(list_of_names)}')


main()

"""This was the output of the build-in 'check50' function"""
# :) adieu.py exists
# :) input of EOF halts program
# :) input of "Liesl" yields "Adieu, adieu, to Liesl"
# :) input of "Liesl" and "Friedrich" yields "Adieu, adieu, to Liesl and Friedrich"
# :) input of "Liesl", "Friedrich", and "Louisa" yields "Adieu, adieu, to Liesl, Friedrich, and Louisa"
# :) input of "Liesl", "Friedrich", "Louisa", and "Kurt" yields "Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt"
# :) input of "Liesl", "Friedrich", "Louisa", "Kurt", and "Brigitta" yields "Adieu, adieu, to Liesl, Friedrich, Louisa,
#    Kurt, and Brigitta"
# :) input of "Liesl", "Friedrich", "Louisa", "Kurt", "Brigitta", "Marta", and "Gretl" yields "Adieu, adieu, to Liesl,
#    Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl"
