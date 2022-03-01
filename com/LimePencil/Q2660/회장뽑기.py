import sys

input = sys.stdin.readline
n = int(input())
graph = [[1000 for _ in range(n+1)]for _ in range(n+1)]
while True:
    a,b = list(map(int,input().split(" ")))
    if a==-1 and b==-1:
        break
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1,n+1):
    graph[k][k] = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
m = float('inf')
ls = []
for i in range(1,n+1):
    a = max(graph[i][1:])
    if a<m:
        ls = [i]
        m = a
    elif m == a:
        ls.append(i)
if m == 1000:
    print("0 0")
else:
    print(str(m) + " "+ str(len(ls)))
    print(*map(str,ls))