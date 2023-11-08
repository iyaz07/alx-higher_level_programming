#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    currentmax = 0
    BEST = 'None'
    for i in a_dictionary:
        if (a_dictionary[i] > currentmax):
            BEST = i
            currentmax = a_dictionary[i]
    return (BEST)
