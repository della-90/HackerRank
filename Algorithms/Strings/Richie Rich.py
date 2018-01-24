#!/bin/python3

import sys

def richieRich(s, n, k):
#    if len(s) == 1:
#        return "9" if k > 0 else s
    
    digits = list(s)
    i = 0
    to_be_replaced = set()
    not_nine = []
    while i < n//2:
        if digits[i] != digits[n-1-i]:
            to_be_replaced.add(i)
        if digits[i] != "9" and digits[n-1-i] != "9":
            not_nine.append(i)
        i += 1
    
    if len(to_be_replaced) > k:
        return -1
    
    # perform replacement
    for x in to_be_replaced:
        digits[x] = max(digits[x], digits[n-1-x])
        digits[n-1-x] = max(digits[x], digits[n-1-x])
        k -= 1
           
    spares = k
    while spares >= 1 and len(not_nine) > 0:
        i = not_nine.pop(0)
        if digits[i] != '9' and (i in to_be_replaced or spares >= 2):
            digits[i] = '9'
            digits[n-1-i] = '9'
            spares -= 2 if i not in to_be_replaced else 1
    
    # if we have "extra" k and the string has an odd length,
    # replace the center with a 9
    if spares > 0 and n%2 != 0:
        digits[n//2] = "9"
        
    return "".join(digits)

n, k = list(map(int, input().strip().split(" ")))
s = input().strip()
result = richieRich(s, n, k)
print(result)
