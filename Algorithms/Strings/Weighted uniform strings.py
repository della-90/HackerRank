#!/bin/python3

import sys

weights = { chr(k + ord('a')):k+1 for k in range(26)}
s = input().strip()
len_s = len(s)
n = int(input().strip())

letters = [0] * len_s
for i in range(len_s):
    if i > 0 and s[i-1] == s[i]:
        letters[i] = letters[i-1]
    letters[i] += weights[s[i]]
letters = set(letters)
for a0 in range(n):
    x = int(input().strip())
    print("Yes" if x in letters else "No")
