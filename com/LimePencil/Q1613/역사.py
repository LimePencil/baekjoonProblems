import sys

input = sys.stdin.readline
n,k = list(map(int,input().split(" ")))
graph = [[0 for _ in range(n+1)]for _ in range(n+1)]
for _ in range(k):
    a,b = list(map(int,input().split(" ")))
    graph[a][b] =1
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][k]==1 and graph[k][j]==1:
                graph[i][j] = 1
s=int(input())
for _ in range(s):
    a,b =list(map(int,input().split(" ")))
    if graph[a][b] == 1:
        print("-1")
    elif graph[b][a] ==1:
        print("1")
    else:
        print("0")