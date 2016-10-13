n, k = map(int, raw_input().split())

s = map(int, raw_input().split())

# a list that counts how many reminders there are
# element "i-th" indicates how many numbers have a remainder of "i"

remainders = [0 for _ in xrange(k)]

for number in s:
    remainders[number % k] += 1

count = min(remainders[0], 1)
for i in xrange(1, 1+k/2):
    if i == k - i:
        count += min(remainders[i], 1)
    else:
        count += max(remainders[i], remainders[k-i])
print count
