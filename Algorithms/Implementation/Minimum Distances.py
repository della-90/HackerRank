#!/bin/python

import sys


n = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))

min_distance = n
for i in xrange(n-1):
    for j in xrange(i+1, n):
        if A[i] == A[j]:
            min_distance = min(min_distance, abs(i-j))
        
print min_distance if min_distance < n else -1
