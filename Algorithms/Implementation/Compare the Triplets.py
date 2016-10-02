#!/bin/python

import sys

a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))

scores = [0, 0]

for i in range(3):
    scores[0] += 1 if a[i] > b[i] else 0
    scores[1] += 1 if b[i] > a[i] else 0

print scores[0], scores[1]
