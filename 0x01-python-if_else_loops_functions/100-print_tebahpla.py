#!/usr/bin/python3
for i in range(0, 26):
    if i % 2 == 0:
        j = 122
    else:
        j = 90
    print("{:c}".format(j - i), end="")
