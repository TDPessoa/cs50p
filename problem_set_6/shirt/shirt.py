"""In a file called shirt.py, implement a program that expects exactly two command-line arguments:

    in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
    in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
    The program should then overlay shirt.png (which has a transparent background) on the input after resizing and
    cropping the input to be the same size, saving the result as its output.

    Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open,
    resize and crop the input with ImageOps.fit,
per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit,
    using default values for method, bleed, and centering,
overlay the shirt with Image.paste, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste,
    and save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:

if the user does not specify exactly two command-line arguments,
if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
if the input’s name does not have the same extension as the output’s name, or
if the specified input does not exist."""

from sys import exit, argv
from PIL import Image, ImageOps


def main():
    try:
        # Checking for the correct quantity of command-line arguments
        if len(argv) == 3:
            # Checking for same file extension
            if argv[1].split('.')[-1] == argv[2].split('.')[-1]:
                # Checking for correct file extension
                if argv[1].split('.')[-1] in ('jpg', 'jpeg', 'png'):
                    with Image.open(argv[1]) as im:
                        # Opening the image to be pasted on the reffered image
                        shirt = Image.open('shirt.png')
                        # Setting the area uppon which the shirt will be pasted
                        area = (0, (shirt.size[0] - shirt.size[1]))
                        # Fitting the main image to a box shape with the width of the shirt image
                        im = ImageOps.fit(im, (shirt.size[0], shirt.size[0]), bleed=0.0, centering=(0.5, 0.5))
                        # Pasting the shirt uppon the image
                        im.paste(shirt, box=area, mask=shirt)
                        # Saving the image with the filename given in the command-line argument
                        im.save(argv[2])

                else:
                    exit('The file extension is not recognizable.')

            else:
                exit("The files extensions don't match.")

        else:
            raise IndexError

    except IndexError:
        exit('Command-line arguments not found or not in accordance')

    # except ValueError
    #     exit('Something went wrong.')

    except FileNotFoundError:
        exit('It was provided an inexisting file in the command-line.')


if __name__ == '__main__':
    main()


"""This was the output of the build-in 'check50' function"""
# :) shirt.py exists
# :) shirt.py exits given zero command-line arguments
# :) shirt.py exits given a file without a .jpg, .jpeg, or .png extension
# :) shirt.py exits given a non-existent file
# :) shirt.py exits given an output file with a different extension than input file
# :) shirt.py exits given more than two command-line arguments
# :) shirt.py correctly displays shirt on muppet_01.jpg
# :) shirt.py correctly displays shirt on muppet_02.jpg
# :) shirt.py correctly displays shirt on muppet_03.jpg
# :) shirt.py correctly displays shirt on muppet_04.jpg
# :) shirt.py correctly displays shirt on muppet_05.jpg
# :) shirt.py correctly displays shirt on muppet_06.jpg
