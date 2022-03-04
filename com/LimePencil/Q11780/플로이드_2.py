import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
path = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a,b,c = list(map(int,input().split(" ")))
    graph[a][b] = min(c,graph[a][b])
    path[a][b] = a

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if i == k or i == j or j==k:
                continue
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                path[i][j] = path[k][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == float('inf'):
            graph[i][j] = 0
    print(*map(str,graph[i][1:]))
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == 0:
            print("0")
        else:
            route = []
            index = j
            while index != i:
                route.append(index)
                index = path[i][index]
            route.append(i)
            route.append(len(route))
            route.reverse()
            print(*map(str,route))