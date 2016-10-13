#!/bin/python

import sys

N = int(raw_input().strip())
B = map(int,raw_input().strip().split(' '))

odds = len(filter(lambda x: x%2 == 1, B))

if odds % 2 != 0:
    print 'NO'
else:
    count = 0
    for i in xrange(N-1):
        if B[i] % 2 != 0:
            count += 2
            B[i] += 1
            B[i+1] += 1
    print count
