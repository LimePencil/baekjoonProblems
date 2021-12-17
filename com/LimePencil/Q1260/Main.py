import sys
from collections import deque
n,m,v =list(map(int,sys.stdin.readline().strip("\n").split(" ")))

graph = [[] * n for _ in range(n+1)]
for i in range(m):
    a, b = list(map(int,sys.stdin.readline().strip("\n").split(" ")))
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
visited = [False]*(n+1)
ans = ""
def dfs(v):
    global visited, graph, ans
    ans += str(v) + " "
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)
dfs(v)
ans += "\n"
visited = [False]*(n+1)
def bfs(v):
    global visited, graph, ans
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        ans += str(v) + " "
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

bfs(v)
sys.stdout.write(ans)

