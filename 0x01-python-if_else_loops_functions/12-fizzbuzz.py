#!/usr/bin/python3
def fizzbuzz():
    for count in range(101):
        if count % 3 == 0:
            print("Fizz ", end="")
        elif count % 5 == 0:
            print("Buzz ", end="")
        elif count % 15 == 0:
            print("FizzBuzz ", end="")
        else:
            print("{:d} ".format(count), end="")
