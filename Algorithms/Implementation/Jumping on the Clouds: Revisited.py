#!/bin/python

import sys


n, k = map(int, raw_input().strip().split(' '))
c = map(int,raw_input().strip().split(' '))

energy = 100
current = 0

def move():
    global current, energy
    current = (current+k)%n
    energy -= 1 if c[current] == 0 else 3
move()
while current != 0:
    move()
print energy


