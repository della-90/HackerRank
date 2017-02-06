import re

pattern = r'^[+-]?\d*\.\d+$'

for _ in range(int(input())):
    print(bool(re.match(pattern, input())))
