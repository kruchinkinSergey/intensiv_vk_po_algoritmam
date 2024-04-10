def has_triangle(graph):
    for vertex in graph:
        neighbors = graph[vertex]
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                if neighbors[i] in graph[neighbors[j]] and neighbors[j] in graph[neighbors[i]]:
                    return True
    return False


n = int(input())  
graph = {}
for _ in range(n):
    v1, v2 = map(int, input().split())
    if v1 not in graph:
        graph[v1] = []
    if v2 not in graph:
        graph[v2] = []
    graph[v1].append(v2)
    graph[v2].append(v1)


result = has_triangle(graph)
if result:
    print("YES")
else:
    print("NO")
