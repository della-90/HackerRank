# Enter your code here. Read input from STDIN. Print output to STDOUT
tests = int(raw_input())
for _ in range(tests):
    n, k = map(int, raw_input().strip().split(" "))
    times = map(int, raw_input().strip().split(" "))
    
    late = 0
    for time in times:
        if time > 0:
            late += 1
        
        if (n - late) < k:
            break
    print 'YES' if (n - late) < k else 'NO'
