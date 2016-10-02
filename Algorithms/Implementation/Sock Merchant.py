#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

socks = {}
for sock in c:
    socks[sock] = 1 if sock not in socks else socks[sock]+1

answer = 0
for sock, amount in socks.iteritems():
    answer += amount/2
    
print answer

