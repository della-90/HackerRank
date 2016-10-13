import re

n, m = map(int, raw_input().split())

matrix = [[c for c in raw_input().strip("\n")] for _ in xrange(n)]
transposed = zip(*matrix)
string = "".join([c for line in transposed for c in line])

string = re.sub(r'(?<=[a-zA-Z\d])[^a-zA-Z\d]+(?=[a-zA-Z\d])', ' ', string)
print string
