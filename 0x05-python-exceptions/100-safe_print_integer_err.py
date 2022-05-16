#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except(ValueError, TypeError) as errors:
        print("Exception: {}".format(errors), file=sys.stderr)
        return False
    return True
