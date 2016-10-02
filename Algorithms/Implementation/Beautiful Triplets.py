# Enter your code here. Read input from STDIN. Print output to STDOUT
n, d = map(int, raw_input().split())
numbers = map(int, raw_input().split())

count = 0
for i in xrange(n):
    if numbers[i] + d in numbers and numbers[i] + 2*d in numbers:
        count += 1
print count
