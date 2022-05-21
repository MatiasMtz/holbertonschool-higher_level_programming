#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer
print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
print(add_integer(0.5783498578734985349857349857973498534987534985734985734957349853489534534, 3))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
