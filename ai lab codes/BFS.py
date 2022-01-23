# Breadth-first search

from collections import defaultdict

graph = defaultdict(list)
visited = []
queue = []


def bfs(node):
    visited.append(node)
    queue.append(node)
    while queue:
        vertex = queue.pop(0)
        print(vertex)
        for adj in graph[vertex]:
            if adj not in visited:
                visited.append(adj)
                queue.append(adj)


print("Enter the number of edges:")
edges = int(input())
print("Enter the edges: ")
for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)

print("Enter the starting node to visit:")
start = int(input())
print("BFS traversal starting from node " + str(start) + ":")
bfs(start)
