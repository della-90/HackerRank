import re

pattern = r'^(?=[4-6])(?!.*?(\d)(-?\1){3})\d{4}(?:-?\d{4}){3}$'
regex = re.compile(pattern)

for _ in xrange(int(raw_input())):
    print 'Valid' if regex.match(raw_input()) else 'Invalid'
