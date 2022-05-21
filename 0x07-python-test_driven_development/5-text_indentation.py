#!/usr/bin/python3
def text_indentation(text):

    if type(text) != str:
        raise TypeError("text must be a string")

    l = 0
    text = text.strip()
    while l < len(text):
        print(text[l], end='')
        if text[l] == '.' or text[l] == '?' or text[l] == ':':
            print('\n')
            if l == len(text) - 1:
                break
            if text[l + 1] == ' ':
                l += 1
            while text[l] == ' ' and text[l + 1] == ' ' and l + 1 < len(text):
                l += 1
        l += 1
