#!/usr/bin/python3
alphabet = 97
while alphabet < 123:
    if alphabet == 101 or alphabet == 113:
        alphabet += 1
        continue
    print(chr(alphabet), end="")
    alphabet += 1
