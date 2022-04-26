#!/usr/bin/python3
for fn in range(10):
    for sn in range(10):
        if fn != sn and fn < sn:
            print(f"{fn:d}{sn:d}, ", end="")
            if fn + sn == 17:
                print(f"{fn:d}{sn:d}")
