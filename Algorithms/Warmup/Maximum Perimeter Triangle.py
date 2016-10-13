n = int(raw_input())
sticks = sorted(map(int, raw_input().split()), reverse=True)

i = 2
while i < n:
    if sticks[i-2] < sticks[i-1] + sticks[i]:
        break
    i += 1
    
if i < n:
    print sticks[i], sticks[i-1], sticks[i-2]
else:
    print -1
