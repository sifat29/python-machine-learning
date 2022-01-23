# Depth-first search

from collections import defaultdict

graph = defaultdict(list)
visited = set()


def dfs(node):
    if node not in visited:
        print(node)
        visited.add(node)
        for adj in graph[node]:
            dfs(adj)


print("Enter the number of edges:")
edges = int(input())
print("Enter the edges: ")
for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)

print("Enter the starting node to visit:")
start = int(input())
print("DFS traversal starting from node " + str(start) + ":")
dfs(start)
