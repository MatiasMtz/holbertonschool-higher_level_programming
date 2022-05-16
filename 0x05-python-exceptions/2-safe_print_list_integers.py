def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for count in range(x):
        try:
            print(f"{my_list[count]:d}", end="")
            count += 1
        except(TypeError, ValueError):
            count = count - 1
            continue
    print()
    return(count)
