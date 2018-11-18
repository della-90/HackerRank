#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    left = 0
    right = len(s) - 1
    while left < right and s[left] == s[right]:
        left += 1
        right -= 1
    if left >= right:
        return -1
    
    inequalityLeft = left
    inequalityRight = right
    
    # let's suppose left is to be removed
    left += 1
    while left < right and s[left] == s[right]:
        left += 1
        right -= 1
        
    return inequalityLeft if left >= right else inequalityRight
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()

