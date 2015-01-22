import re
regex = r'[A-Z]{5}\d{4}[A-Z]'
n = int(input())
for i in range(0, n):
    s = input()
    if (re.match(regex, s)):
        print("YES")
    else:
        print("NO")
