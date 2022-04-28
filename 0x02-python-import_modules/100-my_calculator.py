#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    args = len(argv)
    if args - 1 != 3:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)
    if argv[2] != '+' and argv[2] != '-' and argv[2] != '*' and argv[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == '+':
            print(f"{argv[1]} + {argv[3]} = {add(a, b)}")
        elif argv[2] == '-':
            print(f"{argv[1]} - {argv[3]} = {sub(a, b)}")
        elif argv[2] == '*':
            print(f"{argv[1]} * {argv[3]} = {mul(a, b)}")
        else:
            print(f"{argv[1]} / {argv[3]} = {div(a, b)}")
