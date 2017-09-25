#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
houses = sorted([int(x_temp) for x_temp in input().strip().split(' ')])

def find(houses, n):
    antennas = 0
    i=0
    while i < n:
        lowest = houses[i]
        while (houses[i] - lowest <= k):
            i += 1
            if i == n:
                return antennas + 1
        middle = houses[i-1]
        antennas += 1
        while (houses[i] - middle <= k):
            i += 1
            if i == n:
                return antennas

print(find(houses, n))
