# Enter your code here. Read input from STDIN. Print output to STDOUT
raw_input() # skip 1st line
print reduce(lambda x, y: x+y, map(int, raw_input().split(' ')))

