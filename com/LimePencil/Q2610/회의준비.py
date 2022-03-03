import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[float('inf') for _ in range(n+1)]for _ in range(n+1)]

for _ in range(m):
    a,b= list(map(int,input().split(" ")))
    graph[a][b] =1
    graph[b][a] =1
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i ==j or j==k or i ==k:
                continue
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
visited = [False]*(n+1)
ans = []
for i in range(1,n+1):
    if not visited[i]:
        visited[i] = True
        group = [i]
        for j in range(1,n+1):
            if graph[i][j] !=float('inf'):
                group.append(j)
                visited[j] = True
        min_index = 0
        min_value = float('inf')
        for a in group:
            s = 0
            for b in graph[a]:
                if b != float('inf'):
                    s = max(s,b)
            if min_value>s:
                min_value = s
                min_index = a
        ans.append(min_index)
print(len(ans))
ans.sort()
print("\n".join(map(str,ans)))