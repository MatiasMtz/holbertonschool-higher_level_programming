def safe_print_integer(value):

    try:
        print(f"{value:d}")
    except(ValueError, TypeError):
        return False
    else:
        return True
