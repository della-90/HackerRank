#!/bin/python3

import sys, bisect

n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]

sorted_scores = sorted(list(set(scores)))
size = len(sorted_scores)
for score in alice:
    print(size-bisect.bisect(sorted_scores, score)+1)
