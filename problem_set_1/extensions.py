"""Even though Windows and macOS sometimes hide them, most files have file extensions, a suffix that starts with a
period (.) at the end of their name. For instance, file names for GIFs end with .gif, and file names for JPEGs end with
 .jpg or .jpeg. When you double-click on a file to open it, your computer uses its file extension to determine which
 program to launch.

Web browsers, by contrast, rely on media types, formerly known as MIME types, to determine how to display files that
live on the web. When you download a file from a web server, that server sends an HTTP header, along with the file
itself, indicating the file’s media type. For instance, the media type for a GIF is image/gif, and the media type for
a JPEG is image/jpeg. To determine the media type for a file, a web server typically looks at the file’s extension,
mapping one to the other.

See developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types for common types.

In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that
file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which
is a common default."""


def main():
    exten_list = ['gif', 'jpg', 'jpeg', 'png', 'pdf', 'txt', 'zip']
    type_exten = ['image/gif', 'image/jpeg', 'image/jpeg',
                  'image/png', 'application/pdf', 'text/plain',
                  'application/zip', 'application/octet-stream']
    count = 1
    file_name = str(input("What's the file's name?")).strip().lower()
    for c in range(len(exten_list)):
        if file_name[-3:] in exten_list[c]:
            print(type_exten[c])
            count -= 1
    if count == 1:
        print(type_exten[-1])


main()

"""This was the output of the build-in 'check50' function"""
# :) extensions.py exists
# :) input of cs50.gif yields output of image/gif
# :) input of happy.jpg yields output of image/jpeg
# :) input of happy.jpeg yields output of image/jpeg
# :) input of check.png yields output of image/png
# :) input of document.pdf yields output of application/pdf
# :) input of plain.txt yields output of text/plain
# :) input of files.zip yields output of application/zip
# :) input of application.bin yields output of application/octet-stream
# :) input of document.PDF yields output of application/pdf
# :) input of document.PDF, with spaces on either side, yields output of application/pdf
# :) input of test.txt.pdf, with one extra extension, yields output of application/pdf
# :) input of zipper.jpg, with another extension name, yields output of image/jpeg
# :) input of myfile, with no extension, yields output of application/octet-stream
