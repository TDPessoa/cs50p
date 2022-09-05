"""Suppose that you’d like to implement a CS50 “shirtificate,” a PDF with an image of an I took CS50 t-shirt,
    shirtificate.png, customized with a user’s own name.

    In a file called shirtificate.py, implement a program that prompts the user for their name and outputs,
    using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard,
    with these specifications:

        The orientation of the PDF should be Portrait.
        The format of the PDF should be A4, which is 210mm wide by 297mm tall.
        The top of the PDF should “CS50 Shirtificate” as text, centered horizontally.
        The shirt’s image should be centered horizontally.
        The user’s name should be on top of the shirt, in white text.

    All other details we leave to you. You’re even welcome to add borders, colors, and lines. Your shirtificate needn’t
    match John Harvard’s precisely. And no need to wrap long names across multiple lines.

    Before writing any code, do read through fpdf2’s tutorial to learn how to use it. Then skim fpdf2’s API (application
    programming interface) to see all of its functions and parameters therefor.

    No need to submit any PDFs with your code. But, if you would like, you’re welcome (but not expected) to share a
    shirtificate with your name on it in any of CS50’s communities!"""

from fpdf import FPDF


def main():
    # Requesting name to be printed in the shirt
    name = str(input("What's the name that you'd like?"))

    # Initializing `FPDF`object
    pdf = FPDF()

    # Adding a page to the object
    pdf.add_page()

    # Inserting the shirt image, given by CS50
    pdf.image("shirtificate.png", x=0, y=40)

    # Prepping and printing text `title`
    pdf.set_font("helvetica", style="B", size=50)
    pdf.cell(60, 20, "CS50 Shirtificate")

    # Prepping and printing text `in_shirt`
    pdf.set_font("helvetica", size=26)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(150, 250, f"{name} took CS50")

    # Saving pdf file
    pdf.output('shirtificate.pdf')


if __name__ == "__main__":
    main()


"""This was the output of the build-in 'check50' function"""
# :) shirtificate.py exist
# :) shirtificate.py creates a PDF called shirtificate.pdf
