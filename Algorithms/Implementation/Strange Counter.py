#!/bin/python3

import sys


t = int(input().strip())

counter = 3

while t > counter:
    t -= counter
    counter *= 2
    
print(counter - t + 1)
