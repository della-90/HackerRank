#!/bin/python

import sys


s = raw_input().strip()
n = long(raw_input().strip())

length = len(s)
full = n / length
additional = n % length

count = 0
for c in s:
    count += full if c == 'a' else 0
for i in xrange(additional):
    count += 1 if s[i] == 'a' else 0
    
print count
