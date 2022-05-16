#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for count in range(x):
        try:
            print("{:d}".format(my_list[count]), end="")
            count += 1
        except(TypeError, ValueError):
            count = count - 1
            continue
        except(IndexError)
            break
    print()
    return(count)
