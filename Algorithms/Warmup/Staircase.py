# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())

for i in range(1,n+1):
    print ("#"*i).rjust(n)
