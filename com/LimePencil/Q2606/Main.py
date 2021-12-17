import sys

n = int(sys.stdin.readline().strip("\n"))
m = int(sys.stdin.readline().strip("\n"))

graph = [[] * n for _ in range(n+1)]
for i in range(m):
    a, b = list(map(int,sys.stdin.readline().strip("\n").split(" ")))
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
visited = [False]*(n+1)
ans = -1
def dfs(v):
    global visited, graph, ans
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)
dfs(1)
for i in visited:
    if i == True:
        ans += 1

sys.stdout.write(str(ans))