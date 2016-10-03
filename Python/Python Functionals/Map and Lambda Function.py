# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())

fibonacci = []

for i in xrange(n):
    if i == 0:
        fibonacci.append(0)
    elif i <= 2:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
        
print map(lambda x: x**3, fibonacci)
