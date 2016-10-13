#!/bin/python

import sys
t = int(raw_input().strip())
for _ in xrange(t):
    n, k = map(int, raw_input().strip().split())
    if k == 0:
        print " ".join(str(i) for i in xrange(1, n+1))
    elif n%k != 0:
        print -1
    elif (n/k)%2 != 0:
        print -1
    else:
        acc = 0
        for i in xrange(1, n+1):
            print i+k if 0 <= acc else i-k,
            acc += 1
            if acc == k:
                acc = -k
        print ''
