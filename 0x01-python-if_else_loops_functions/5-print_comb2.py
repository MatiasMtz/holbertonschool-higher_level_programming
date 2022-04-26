#!/usr/bin/python3
for number in range(100):
    if number == 99:
        print("{:d}".format(number))
        break
    print("{:02d}, ".format(number), end="")
