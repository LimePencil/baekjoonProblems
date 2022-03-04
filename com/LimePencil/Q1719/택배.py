import sys

input = sys.stdin.readline
n,m = list(map(int,input().split(" ")))
graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
path = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a,b,c = list(map(int,input().split(" ")))
    graph[a][b] = c
    graph[b][a] = c
    path[a][b] = b
    path[b][a] = a

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if i == k or i == j or j==k:
                continue
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                path[i][j] = path[i][k]

for i in range(1,n+1):
    path[i][i] = "-"
    print(*map(str,path[i][1:]))