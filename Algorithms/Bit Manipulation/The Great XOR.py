#!/bin/python3

import sys

def theGreatXor(x):
    bits = format(x, 'b')
    has_one = False
    msb = len(bits) - 1
    result = 0
    for index, bit in enumerate(bits):
        if bit == '1' and not has_one:
            has_one = True
        elif bit == '0' and has_one:
            result += 2**(msb-index) if msb-index > 0 else 1
    return result

q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    result = theGreatXor(x)
    print(result)
