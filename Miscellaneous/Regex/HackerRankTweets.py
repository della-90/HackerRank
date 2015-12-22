import re
regex = r'(?:[#@])?hackerrank'

n = int(input())
count = 0
for i in range(0, n):
    s = input()
    groups = re.findall(regex, s, re.I)
    if (groups):
        count += len(groups)
print(count)
