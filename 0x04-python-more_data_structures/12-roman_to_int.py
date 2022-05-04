#!/usr/bin/python3
def roman_to_int(roman_string):
    num_map = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    i = 0
    total = 0
    if isinstance(roman_string, str):
        for i in range(len(roman_string) - 1):
            if num_map[roman_string[i]] >= num_map[roman_string[i + 1]]:
                total += num_map[roman_string[i]]
            else:
                total -= num_map[roman_string[i]]
            i += 1
        total += num_map[roman_string[i]]
        return total
    return 0
