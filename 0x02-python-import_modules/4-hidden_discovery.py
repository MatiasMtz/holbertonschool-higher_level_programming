#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for count in range(1, len(names)):
        if names[count][0] != "_" and names[count][1] != "_":
            print(f"{names[count]}")
