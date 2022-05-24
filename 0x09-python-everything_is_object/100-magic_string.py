#!/usr/bin/python3
def magic_string():
    setattr(magic_string, "nTimes", getattr(magic_string, "nTimes", -1) + 1)
    return "BestSchool" + ", BestSchool" * getattr(magic_string, "nTimes", 0)
