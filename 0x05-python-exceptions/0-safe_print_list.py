#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    count = 0

    for i in my_list:
        i = i + 1
    while count <= (x - 1) and count <= i:
        try:
            print(f"{my_list[count]}", end="")
            count = count + 1
        except IndexError:
            break
    print()
    return(count)
