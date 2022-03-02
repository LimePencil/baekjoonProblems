import sys

def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or i==k or j == k:
                    continue
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    return -1
                if graph[i][j] == graph[i][k] + graph[k][j]:
                    road[i][j] = 0
    return 0
                


input = sys.stdin.readline
n = int(input())
graph = []
road = [[1 for _ in range(n)]for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int,input().split(" "))))
a = floyd()
if a != -1:
    ans = 0
    for i in range(n):
        for j in range(n):
            if road[i][j] == 1:
                ans += graph[i][j]
    print(ans//2)
else:
    print(-1)