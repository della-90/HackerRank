#!/bin/python3

import sys

def findComponents(graph):
    visited = set()
    stack = []
    result = []
    
    for u in range(len(graph)):
        if u in visited:
            continue
        stack.append(u)
        current = 0
        while len(stack) > 0:
            v = stack.pop()
            if v in visited:
                continue
            current += 1
            visited.add(v)
            adjacents = list(filter(lambda x: x not in visited, graph[v]))
            stack.extend(adjacents)
        result.append(current)
        
    return result

q = int(input().strip())
for _ in range(q):
    n, m, clib, croad = list(map(int, input().strip().split()))
    
    # if schools are cheaper than or as expensive as roads,
    # then let's put schools in all the cities
    if clib <= croad or m == 0:
        # consume input
        for _ in range(m):
            input()
        print(clib*n)
        continue
    
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = list(map(int, input().strip().split()))
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
        
    components = findComponents(graph)
    
    # for each component count the nodes
    # to connect the component we need n-1 edges at least
    cost = 0
    for component in components:
        nodes = component
        # for each component we need 1 school and n-1 roads
        cost += clib
        cost += (nodes-1)*croad
    print(cost)
