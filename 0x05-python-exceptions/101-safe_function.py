#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as errors:
        print("Exception: {}".format(errors), file=sys.stderr)
        return None
    return result
