import re
n = int(input())
pattern = r'[a-z]{,3}\d{2,8}[A-Z]{3,}'
regex = re.compile(pattern)
for _ in range(0, n):
    s = input()
    if (regex.match(s)):
        print('VALID')
    else:
        print('INVALID')
    
