#!/bin/python

import sys

def check(G, R, C, g, r, c, I, J):
    """
    I = start index of the row
    J = start index of the col
    """
    for y in xrange(I, I+r):
        for x in xrange(J, J+c):
            if G[y][x] != g[y-I][x-J]:
                return False
    return True

def search(G, R, C, g, r, c):
    I = J = i = j = 0

    # Search start point
    while I <= R-r:
        while J <= C-c:
            result = check(G, R, C, g, r, c, I, J)
            if result:
                return True
            J += 1
        I += 1
        J = 0
    return False
    
t = int(raw_input().strip())
for a0 in xrange(t):
    R, C = map(int, raw_input().strip().split())
    G = []
    for i in xrange(R):
        line = raw_input().strip()
        G.append([int(n) for n in line])   
            
    r, c = map(int, raw_input().strip().split())
    g = []
    for x in xrange(r):
        line = raw_input().strip()
        g.append([int(n) for n in line])   
    
    print 'YES' if search(G, R, C, g, r, c) else 'NO'
