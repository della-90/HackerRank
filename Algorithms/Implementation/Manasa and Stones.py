# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
for _ in xrange(t):
    n = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
    
    result = set()
    for i in xrange(n):
        result.add(a*i + (n-1-i)*b)
    print " ".join([str(n) for n in sorted(result)])
