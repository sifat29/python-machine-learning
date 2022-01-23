from collections import defaultdict

graph = defaultdict(list)
elem = []


def dls(src, node, depth):
    if src == node:
        return True
    if depth <= 0:
        return False
    for i in graph[src]:
        if dls(i, node, depth - 1):
            # print(i)
            elem.append(i)
            return True

    return False


def operateDFS(src, node, depth):
    for i in range(depth):
        if dls(src, node, i):
            return True

    return False


print("Enter the number of edges:")
edges = int(input())
print("Enter the edges: ")
for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)

print("Enter the target:")
target = int(input())
print("Enter the maximum depth:")
maxDepth = int(input())
print("Enter the source:")
source = int(input())

if operateDFS(source, target, maxDepth):
    print("Target can be reached from " + str(source) + " within " + str(maxDepth) + " maximum depth")
    elem.append(source)
    elem.sort()
    print("Traversal:", elem)
else:
    print("Target can't be reached from " + str(source) + " within " + str(maxDepth) + " maximum depth")
