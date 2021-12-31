import sys

graph = {}
n = int(sys.stdin.readline().rstrip("\n"))
for _ in range(n-1):
    a,b = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)
    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)
stack = [1]
visited = [False]*n
parent = [0]*n
while stack:
    a = stack.pop()
    if not visited[a-1]:
        visited[a-1] = True
        for c in graph[a]:
            stack.append(c)
            if not visited[c-1]:
                parent[c-1] = a
print(*parent[1:])


