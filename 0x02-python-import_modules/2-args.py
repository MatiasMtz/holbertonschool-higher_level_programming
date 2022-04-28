#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv)
    if arg_count == 1:
        print(f"{arg_count - 1} arguments.")
    elif arg_count == 2:
        print(f"{arg_count - 1} argument:")
    else:
        print(f"{arg_count - 1} arguments:")
    for count in range(1, arg_count):
        print(f"{count}: {sys.argv[count]}")
