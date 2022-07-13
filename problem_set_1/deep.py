"""“All right,” said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.
“You’re really not going to like it,” observed Deep Thought.
“Tell us!”
“All right,” said Deep Thought. “The Answer to the Great Question…”
“Yes…!”
“Of Life, the Universe and Everything…” said Deep Thought.
“Yes…!”
“Is…” said Deep Thought, and paused.
“Yes…!”
“Is…”
“Yes…!!!…?”
“Forty-two,” said Deep Thought, with infinite majesty and calm.”

— The Hitchhiker’s Guide to the Galaxy, Douglas Adams

In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and
Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No."""


def main():
    answer = str(
        input('What is The Answer to the Great Question Of Life, the Universe and Everything?')).strip().lower()
    if answer == '42' or \
            answer == 'forty-two' or \
            answer == 'forty two':
        print('yes')
    else:
        print('no')


main()

"""This was the output of the build-in 'check50' function"""
# :) deep.py exists
# :) input of 42 yields output of Yes
# :) input of forty-two yields output of Yes
# :) input of forty two yields output of Yes
# :) input of FoRty TwO yields output of Yes
# :) input of 42, with spaces on either side, yields output of Yes
# :) input of 50 yields output of No
# :) input of fifty yields output of No
