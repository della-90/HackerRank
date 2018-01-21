#!/bin/python3

import sys

def separateNumbers(s):
    for first_number_length in range(1, 1+len(s)//2):
        n = int(s[:first_number_length])
        remainder = s[first_number_length:]
        expected = n+1
        while len(remainder) > 0:
            if remainder.startswith(str(expected)):
                remainder = remainder[len(str(expected)):]
                expected += 1
            else:
                break
        if len(remainder) == 0:
            print("YES " + str(n))
            return
    print("NO")

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        separateNumbers(s)
