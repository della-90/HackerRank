raw_input()
m = set(map(int, raw_input().split()))
raw_input()
n = set(map(int, raw_input().split()))

print "\n".join(str(x) for x in sorted(list((m-n)|(n-m))))
