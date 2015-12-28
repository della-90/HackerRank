from math import *

plain = input()
length = len(plain)
l = sqrt(length)
rows = int(floor(l))
cols = int(ceil(l))
for i in range(cols):
    j = i
    while j<length:
        print(plain[j], end="")
        j += cols
    print(" ", end="")
