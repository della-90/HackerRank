from collections import deque
for _ in xrange(int(raw_input())):
    n = int(raw_input())
    cubes = deque(map(int, raw_input().split()))
    
    last = max(cubes[0], cubes[-1])
    while len(cubes) > 0:
        next = max(cubes[0], cubes[-1])
        if next <= last:
            last = next
            if cubes[0] > cubes[-1]:
                cubes.popleft()
            else:
                cubes.pop()
        else:
            break
    print 'Yes' if len(cubes) == 0 else 'No'
        
