#!/usr/bin/python3
def remove_char_at(str, n):
    for num in range(len(str)):
        if num != n:
            new_str += str[num]

    return new_str
