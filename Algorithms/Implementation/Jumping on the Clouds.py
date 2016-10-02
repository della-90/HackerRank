#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

current = 0
moves = 0
while current < n-1:
    current += 2 if current <= n-3 and c[current+2] == 0 else 1
    moves += 1
    
print moves
