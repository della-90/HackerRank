#!/bin/python

import sys


n = int(raw_input().strip())
for _ in xrange(n):
    s = raw_input().strip()
    
    # the minimum cost is to add each new different letter (we can reuse the others)
    print len(set(s))
