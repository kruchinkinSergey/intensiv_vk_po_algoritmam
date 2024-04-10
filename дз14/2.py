# n = int(input())  
# graph = {}
# for _ in range(n):
#     v1, v2 = map(int, input().split())
#     if v1 not in graph:
#         graph[v1] = []
#     if v2 not in graph:
#         graph[v2] = []
#     graph[v1].append(v2)
#     graph[v2].append(v1)

# def has_triangle(graph):
#     soc_circle_cnt = 0
#     for i in range(1, len(graph)):
#         last_neighbor = graph[i][-1]
#         if last_neighbor == graph[i+1]:
#             continue
#         else:
#             soc_circle_cnt += 1

#     return soc_circle_cnt

# print(has_triangle(graph))
    
# graph = {1: [2], 2: [1, 3], 3: [2, 4], 4: [3], 5: [6], 6: [5]}
# for i in range(1, len(graph) + 1):
#     print(graph[i][-1])

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

def dfs(v, visited, graph):
    visited.add(v)
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(neighbor, visited, graph)

def count_social_circles(graph):
    visited = set()
    soc_circle_cnt = 0
    for v in graph:
        if v not in visited:
            dfs(v, visited, graph)
            soc_circle_cnt += 1

    return soc_circle_cnt

print(count_social_circles(graph))