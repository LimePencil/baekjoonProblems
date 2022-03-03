import sys

input = sys.stdin.readline
n,m = list(map(int,input().split(" ")))
graph = [[float('inf') for _ in range(n+1)]for _ in range(n+1)]
for _ in range(m):
    s,e = list(map(int,input().split(" ")))
    graph[s][e] = 1
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                continue
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
half = (n+1)//2
count = 0
for i in range(1,n+1):
    lower = 0
    upper = 0
    for j in range(1,n+1):
        if i == j:
            continue
        if graph[i][j] != float('inf'):
            lower +=1
        if graph[j][i] != float('inf'):
            upper +=1
    if max(lower,upper) >= half:
        count+=1
print(count)