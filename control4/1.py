def bellman_ford(edges, num_vertices, src):
    dist = [float("Inf")] * num_vertices
    dist[src] = 0

    for _ in range(num_vertices - 1):
        for u, v, w in edges:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            print("Граф содержит отрицательный цикл")
            return

    print("Результаты:")
    for i in range(num_vertices):
        print(f"Вершина: {i+1}, Расстояние: {dist[i]}")


# Ввод данных
num_edges = int(input())
edges = []
for _ in range(num_edges):
    u, v, w = map(int, input().split())
    edges.append((u-1, v-1, w))

num_vertices = max(max(u, v) for u, v, _ in edges) + 1
src_vertex = int(input()) - 1

bellman_ford(edges, num_vertices, src_vertex)