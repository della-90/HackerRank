#!/bin/python

import sys
    

t = int(raw_input().strip())
for _ in xrange(t):
    n = int(raw_input().strip())
    # If n is not divisible by 3, than subtract 5 to n until it
    # becomes a multiple of 3 (at most two subtractions)

    tmp = n # tmp = number of '5's, (n-tmp) = number of '3's
    while tmp%3 != 0:
        tmp -= 5
    print '5'*tmp+'3'*(n-tmp) if tmp >= 0 else '-1'
    
