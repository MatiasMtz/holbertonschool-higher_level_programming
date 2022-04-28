#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    if len(sys.argv) == 1:
        print("0")
    else:
        for count in range(1, len(sys.argv)):
            add += int(sys.argv[count])
        print(f"{add:d}")
