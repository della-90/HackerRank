# Enter your code here. Read input from STDIN. Print output to STDOUT
n, k = map(int, raw_input().split())
luck = 0
important_contests = []

for _ in xrange(n):
    l, t = map(int, raw_input().split())
    if t == 0:
        luck += l
    else:
        important_contests.append(l)
        
important_contests.sort(reverse=True)

for i in xrange(len(important_contests)):
    if i < k:
        luck += important_contests[i]
    else:
        luck -= important_contests[i]
        
print luck
    
