s = raw_input()
k = int(raw_input())

tokens = [s[k*i:k*(i+1)] for i in xrange(len(s) / k)]

for token in tokens:
    alreadyUsed = set()
    result = []
    for c in token:
        if c not in alreadyUsed:
            alreadyUsed.add(c)
            result.append(c)
    print ''.join(result)
