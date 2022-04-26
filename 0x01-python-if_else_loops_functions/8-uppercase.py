#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        lower = 0
        ascii_value = ord(letter)
        if ascii_value > 96 and ascii_value < 123:
            lower = 32
        print("{}".format(chr(ascii_value - lower)), end="")
    print()
