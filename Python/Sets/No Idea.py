raw_input()

array = map(int, raw_input().split())
a = set(int(x) for x in raw_input().split())
b = set(int(x) for x in raw_input().split())

happiness = 0
for n in array:
    happiness += 1 if n in a else -1 if n in b else 0
print happiness
