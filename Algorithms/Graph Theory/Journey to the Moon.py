n, p = list(map(int, input().strip().split()))

# adjacency list
graph = [[] for _ in range(n)]
non_singletons = set()

def findConnectedComponents(graph):
    stack = []
    visited = set()
    result = []
        
    for i in non_singletons:
        stack.append(i)
        current = 0
        while len(stack) > 0:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            current += 1

            following = graph[node]
            stack.extend(list(filter(lambda x: x not in visited, following)))
        if current > 0:
            result.append(current)
    
    return result

for _ in range(p):
    a, b = list(map(int, input().strip().split()))
    
    # add new adjacency
    graph[a].append(b)
    graph[b].append(a)
    
    non_singletons.add(a)
    non_singletons.add(b)
    
components = findConnectedComponents(graph)

singletons = n - len(non_singletons)

result = singletons*(singletons-1)//2
for i in range(len(components)):
    result += components[i]*(sum(components[i+1:]) + singletons)
    
print(result)
