# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())

total = 0
for i in range(n):
    row = map(int, raw_input().split(' '))
    total += row[i]
    total -= row[n-i-1]
print abs(total)
