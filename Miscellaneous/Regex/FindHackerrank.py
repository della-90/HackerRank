import re
regex = r"(.*?)hackerrank(.*)"

rows = int(input())
for i in range(0, rows):
    s = input()
    match = re.match(regex, s)
    if (match):
        g1 = len(match.group(1))
        g2 = len(match.group(2))
        if (g1 > 0 and g2 > 0):
            print(-1)
        elif (g2 > 0):
            print(1)
        elif (g1 > 0):
            print(2)
        else:
            print(0)
    
