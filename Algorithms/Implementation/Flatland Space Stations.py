#!/bin/python

import sys


n, m = map(int, raw_input().split())
c = sorted(map(int,raw_input().split()))

if len(c) == 1:
    print max(n-1-c[0], c[0])
else:
    result = 0
    for i in xrange(len(c)-1):
        result = max(result, (c[i+1] - c[i]) / 2)
    result = max(result, c[0], n-1-c[-1])
    print result
