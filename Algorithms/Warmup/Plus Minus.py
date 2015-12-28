# Enter your code here. Read input from STDIN. Print output to STDOUT
n = float(raw_input())
numbers = map(int, raw_input().split(' '))
positives = 0
zeros = 0
for num in numbers:
    if num > 0:
        positives += 1
    elif num == 0:
        zeros += 1
print positives/n
print (n-positives-zeros)/n
print zeros/n
