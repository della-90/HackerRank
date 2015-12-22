import re
pattern = r'(?:https?|ftp)(?:\:\/\/|(?:\%\w{2}){3})(?:www2?\.)?(?P<domain>(?:(?:[-\w]+|(?:\%\w{2})+)\.)+[^\W_]{2,6})'
regex = re.compile(pattern)
n = int(raw_input())
matches = set()
for _ in range(n):
    line = raw_input()
    matches.update(regex.findall(line))
print ';'.join(sorted(matches))
