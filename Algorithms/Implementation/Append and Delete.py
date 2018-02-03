#!/bin/python3

import sys

def appendAndDelete(s, t, k):
    if len(s) + len(t) < k:
        # we can delete all "s" and write all "t"
        return "Yes"
    
    i = 0
    # find the index where "s" and "t" diverge
    limit = min(len(s), len(t))
    while i < limit and s[i] == t[i]:
        i += 1
        
    difference = max(-1, k-(len(s) - i + len(t) - i))
    return "Yes" if 0 == difference % 2  else "No"
        

if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    print(result)
