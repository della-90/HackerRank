import collections

n = int(input())
a = [*map(int, input().split(' '))]
counter = collections.Counter(a)

print(n-counter.most_common(1)[0][1])
