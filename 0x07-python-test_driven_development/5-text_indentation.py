#!/usr/bin/python3
"""
"5-text_indentation" module.

The 5-text_indentation module supplies the function text_indentation
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ?
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace(". ", ".")
    text = text.replace("? ", "?")
    text = text.replace(": ", ":")
    for i in text:
        if i == '.':
            i = '.\n\n'
        elif i == '?':
            i = '?\n\n'
        elif i == ':':
            i = ':\n\n'
        print(i, end="")
