#!/bin/python3

import sys
import collections

def isValid(s):
    frequencies = collections.Counter(s)
    distinct_numbers = set(frequencies.values())
    if len(distinct_numbers) == 1:
        return "YES"
    if len(distinct_numbers) > 2:
        return "NO"
    # count the how many numbers we have for each frequency
    most_frequent, least_frequent = collections.Counter(frequencies.values()).most_common(2)
    # most_frequent and least_frequent are in form: (number, frequency)
    return "YES" if least_frequent[1] == 1 and least_frequent[0] in [1, most_frequent[0]+1] else "NO"

s = input().strip()
result = isValid(s)
print(result)
