# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in xrange(int(raw_input())):
    n, m, s = map(int, raw_input().split())
    print (s+m - 2)%n + 1

