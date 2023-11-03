#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    cast = dir(hidden_4)
    for i in cast:
        if i[:2] != "__":
            print(i)
