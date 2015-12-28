# Enter your code here. Read input from STDIN. Print output to STDOUT
p = int(raw_input())
q = int(raw_input())

result = []
for i in range(p, q+1):
    square = i**2
    length = len(str(square))
    if length > 1: 
        left = int(str(square)[:length/2])
    else:
        left = 0
    right = int(str(square)[length/2:])
    if left+right == i:
        result.append(str(i))
if result:
    print " ".join(result)
else:
    print "INVALID RANGE"
