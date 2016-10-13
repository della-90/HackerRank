#!/bin/python

import sys
import re


s_len = int(raw_input().strip())
s = raw_input().strip()

pattern = r'^(?=([a-z])([a-z]))(?:\1\2)*\1\2?$'
regex = re.compile(pattern)

def matches(x):
    return regex.match(x) != None

chars = [(a, b) for a in set(s) for b in set(s) if a < b]

solution = 0
for a, b in chars:
    temp = re.sub(r'[^%s%s]' % (a, b), '', s)
    if matches(temp):
        solution = max(solution, len(temp))
    
print solution
