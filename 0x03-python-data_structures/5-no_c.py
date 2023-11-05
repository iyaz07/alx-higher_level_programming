#!/usr/bin/env python3
def no_c(my_string):
    valid_str = ''
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            valid_str += ch
        return (valid_str)
