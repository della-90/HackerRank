n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

k = int(input())

data.sort(key=lambda x: x[k])

print("\n".join(" ".join(str(elem) for elem in row) for row in data))
