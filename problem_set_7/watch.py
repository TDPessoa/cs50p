"""It turns out that (most) YouTube videos can be embedded in other websites, just like the above.
For instance, if you visit https://youtu.be/xvFZjo5PgG0 on a laptop or desktop, click Share, and
then click Embed, you’ll see HTML (the language in which web pages are written) like the below,
which you could then copy into your own website’s source code, wherein iframe is an HTML
“element,” and src is one of several HTML “attributes” therein, the value of which, between quotes,
is https://www.youtube.com/embed/xvFZjo5PgG0.

<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube
video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
gyroscope; picture-in-picture" allowfullscreen></iframe>
Because some HTML attributes are optional, you could instead minimally embed just the below.

<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
Suppose that you’d like to extract the URLs of YouTube videos that are embedded in pages (e.g.,
https://www.youtube.com/embed/xvFZjo5PgG0), converting them back to shorter, shareable youtu.be
URLs (e.g., https://youtu.be/xvFZjo5PgG0) where they can be watched on YouTube itself.

In a file called watch.py, implement a function called parse that expects a str of HTML as input,
extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, and
returns its shorter, shareable youtu.be equivalent as a str. Expect that any such URL will be in
one of the formats below. Assume that the value of src will be surrounded by double quotes. And
assume that the input will contain no more than one such URL. If the input does not contain any
such URL at all, return None.

http://youtube.com/embed/xvFZjo5PgG0
https://youtube.com/embed/xvFZjo5PgG0
https://www.youtube.com/embed/xvFZjo5PgG0
Structure watch.py as follows, wherein you’re welcome to modify main and/or implement other
functions as you see fit, but you may not import any other libraries. You’re welcome, but not
required, to use re and/or sys."""

from re import search


def main():
    # Asking for the embeded tag
    phrase = str(input("What's the embedded tag?"))
    # Checking for the right typo in the input:
    # It was structured as: <"-(*4|5)~~~(*3)-(*n)~(*0|1)'youtube.com/embed/'"-|~(*n)>
    # Where:
    # -[\w] stands for letters;
    # ~[\W] stands for characters different from letters; and
    # (), * and n are for repetitions
    # enclosed in () and multiplied[*] by any[n] or the value given
    if search(r'\"\w{4,5}\W{3}\w*\W?youtube.com/embed/.+".*\"', phrase):
        print(parse(phrase))

    else:
        print(None)


def parse(phrase):
    # Checking if the str contains the tag template
    if phrase.startswith('<iframe') and phrase.endswith('></iframe>'):

        # Spliting the str by '"' returns a list of 3 elements, and one of which will be the url
        phrase = phrase.split('"')
        for n in phrase:

            # Checking if the current string has 'youtube' in it's content
            if 'youtube' in n:
                # Getting the value from the last item in n splited by '/'
                return f'https://youtu.be/{n.split("/")[-1]}'

    # If all others pass, this kicks, returning value 'None'
    return None


if __name__ == '__main__':
    main()

"""This was the output of the build-in 'check50' function"""
# :) watch.py exists
# :) watch.py extracts http:// formatted link from iframe with single attribute
# :) watch.py extracts https:// formatted link from iframe with single attribute
# :) watch.py extracts https://www. formatted link from iframe with single attribute
# :) watch.py extracts http:// formatted link from iframe with multiple attributes
# :) watch.py extracts https:// formatted link from iframe with multiple attributes
# :) watch.py extracts https://www. formatted link from iframe with multiple attributes
# :) watch.py returns None when given iframe without YouTube link
# :) watch.py returns None when given YouTube link outside of an iframe