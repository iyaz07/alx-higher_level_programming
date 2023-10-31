#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        char = ord(str[i])
        if char > 96 and char < 123:
            char = char - 32
        print("{:c}".format(char), end="")
    print(end="\n")
