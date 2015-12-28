# Enter your code here. Read input from STDIN. Print output to STDOUT
raw_input()
print reduce(lambda x, y: x+y, map(int, raw_input().split()))
