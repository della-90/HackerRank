#!/bin/python

import sys
import string

n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

result = ""
num_letters = len(string.ascii_lowercase)
for c in s:
    if c in string.ascii_lowercase:
        index = (string.ascii_lowercase.index(c) + k) % num_letters
        result += string.ascii_lowercase[index]
    elif c in string.ascii_uppercase:
        index = (string.ascii_uppercase.index(c) + k ) % num_letters
        result += string.ascii_uppercase[index]
    else:
        result += c
print result
