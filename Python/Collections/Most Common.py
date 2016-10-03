def compare(x, y):
    if frequences[x] == frequences[y]:
        return ord(x)-ord(y)
    return frequences[y] - frequences[x]

s = raw_input()
frequences = {}
for c in s:
    if c in frequences:
        frequences[c] += 1
    else:
        frequences[c] = 1
        
letters = frequences.keys()
letters.sort(cmp=compare)

for i in range(min(len(letters), 3)):
    l = letters[i]
    print l, frequences[l] 
