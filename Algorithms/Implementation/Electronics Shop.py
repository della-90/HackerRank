#!/bin/python3

import itertools

def getMoneySpent(keyboards, drives, s):    
    combined = filter(lambda x: sum(x) <= s, itertools.product(keyboards, drives))
    affordable = sorted(list(combined), key=sum, reverse=True)
    if len(affordable) == 0:
        return -1
    else:
        return sum(affordable[0])

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
