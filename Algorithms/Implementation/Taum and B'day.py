# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
for _ in range(t):
    b, w = map(int, raw_input().strip().split(' '))
    x, y, z = map(int, raw_input().strip().split(' '))
    
    nb = 0 # num black
    nw = 0 # num white
    nt = 0 # transforms
    
    if (x > y + z):
        nw = w+b
        nt = b
    elif (y > x + z):
        nb = b+w
        nt = w
    else:
        nb = b
        nw = w
    
    print (nb*x + nw*y +nt*z)
