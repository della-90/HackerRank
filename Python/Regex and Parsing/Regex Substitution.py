import re

pattern = r'(?<=\s)(&|\|)\1(?=\s)'

for _ in xrange(int(raw_input())):
    print re.sub(pattern, lambda x: "and" if x.group(0) == '&&' else 'or', raw_input())
