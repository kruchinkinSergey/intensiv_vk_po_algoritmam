from collections import deque

def bfs_with_transfers(graph, start, end):
    visited = set()
    queue = deque([(start, 0)])  # Добавляем количество пересадок в очередь
    visited.add(start)

    while queue:
        node, transfers = queue.popleft()

        if node == end:
            return transfers

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_transfers = transfers + 1 if neighbor != end else transfers
                queue.append((neighbor, new_transfers))

    return "No path found"

# Чтение входных данных
N = int(input())
graph = {}
for _ in range(N):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

start, end = map(int, input().split())

# Вызов функции для поиска пути с минимальным количеством пересадок
result = bfs_with_transfers(graph, start, end)
print(result)
