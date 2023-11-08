#!/usr/bin/python3
def roman_to_int(roman_string):
    if ((not roman_string) or not (isinstance(roman_string, str))):
        return 0
    romanList = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(0, len(roman_string)):
        if (i > 0 and romanList[roman_string[i]] > romanList[roman_string[i - 1]]):
            total += romanList[roman_string[i]] - (2 * romanList[roman_string[i - 1]])
        else:
            total += romanList[roman_string[i]]
    return (total)