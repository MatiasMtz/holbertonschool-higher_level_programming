#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    value = list(a_dictionary.keys())[0]
    big = a_dictionary[value]
    for i, v in a_dictionary.items():
        if v > big:
            big = v
            value = i
    return (value)
