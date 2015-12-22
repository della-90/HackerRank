# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import string
from pprint import pprint

# creates a list without duplicates from iterable s
def distinctList(s):
    seen = set()
    return [c for c in s if c not in seen and not seen.add(c)]
    
n = int(raw_input())
for _ in range(n):
    # create list without duplicates
    key = distinctList(raw_input())
    ciphertext = raw_input()
  
    alph = [c for c in string.ascii_uppercase if c not in key]
    matrix = [[c] for c in key]
    for i in range(len(alph)):
        matrix[i%len(key)].append(alph[i])
    
    # sort matrix based on first row
    matrix = sorted(matrix, key=lambda x: x[0]) # x is the i-th element of matrix
    
    # make matrix flat
    matrix = [item for sublist in matrix for item in sublist]

    # create substitution cipher->plain
    sub = {}
    index = 0
    for c in matrix:
        sub[c] = string.ascii_uppercase[index]
        index += 1
    
    # print plaintext
    for c in ciphertext:
            sys.stdout.write(sub.get(c,c))
    print ''
