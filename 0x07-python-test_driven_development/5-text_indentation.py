#!/usr/bin/python3
"""Module that prints a text with 2 new lines after each of
these characters: ., ? and :"""


def text_indentation(text):
    """
    Args:
    text (str): String that will be splitted
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    i = 0
    text = text.strip()
    while i < len(text):
        print(text[i], end='')
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print('\n')
            if i == len(text) - 1:
                break
            if text[i + 1] == ' ':
                i += 1
            while text[i] == ' ' and text[i + 1] == ' ' and i + 1 < len(text):
                i += 1
        i += 1
