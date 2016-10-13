import re

pattern = r'^[1-9]\d{5}$'
regex = re.compile(pattern)

line = raw_input()

first_match = bool(regex.match(line))
second_match = len(re.findall(r'(?=(\d)\d\1)', line)) <= 1

print first_match and second_match
