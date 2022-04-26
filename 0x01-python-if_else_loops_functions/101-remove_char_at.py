#!/usr/bin/python3
def remove_char_at(str, n):
    strdup = str
    if n < 0:
        n = len(str) + 1
    strdup = strdup[:n] + strdup[n+1:]
    return(strdup)
