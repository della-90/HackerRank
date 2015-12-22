import re
n = int(input())
pattern = r'hi\s(?!d).+'
regex = re.compile(pattern, re.I)

for _ in range(0, n):
    s = input()
    if (regex.match(s)):
        print(s)
