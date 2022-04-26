#!/usr/bin/python3
for fn in range(10):
    for sn in range(10):
        if fn != sn and fn < sn:
            if fn + sn == 17:
                print("{:d}{:d}".format(fn, sn))
                break
            print("{:d}{:d}, ".format(fn, sn), end="")
