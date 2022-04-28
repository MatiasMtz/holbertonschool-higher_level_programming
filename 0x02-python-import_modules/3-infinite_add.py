#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    if len(sys.argv) == 1:
        print("0")
    #elif len(sys.argv) == 2:
    #    number = int(sys.argv[1])
    #    print(f"{number:d}")
    else:
        for count in range(1, len(sys.argv)):
            add += int(sys.argv[count])
        print(f"{add:d}")
