#!/usr/bin/python3
import calculator_1
if __name__ == "__main__":
a = 10
b = 5
print(f"{a} + {b} = {calculator_1.add(a, b)}")
print(f"{a} - {b} = {calculator_1.sub(a, b)}")
print(f"{a} * {b} = {calculator_1.mul(a, b)}")
print(f"{a} / {b} = {calculator_1.div(a, b)}")
