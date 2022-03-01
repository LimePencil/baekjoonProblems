import sys

input = sys.stdin.readline
n = int(input())
graph = [[float('inf') for _ in range(n)]for _ in range(n)]
for i in range(n):
    s = input().rstrip("\n")
    for j in range(n):
        if s[j] =="Y":
            graph[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if graph[i][k]+graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k]+graph[k][j]
m = 0
for i in range(n):
    count = 0
    for j in range(n):
        if graph[i][j] <=2:
            count+=1
    m = max(count,m)
print(m)