import sys
from collections import deque

def BFS():
    queue = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    c =[[0 for _ in range(m)] for _ in range(n)]
    queue.append((0,0))
    visited[0][0] = True
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            n_x = direction[i][0]+x
            n_y = direction[i][1]+y
            if 0<=n_x<n and 0<=n_y<m and not visited[n_x][n_y]:
                if graph[n_x][n_y] == 0:
                    visited[n_x][n_y] = True
                    queue.append((n_x,n_y))
                else:
                    c[n_x][n_y] +=1
    return c

n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
graph = []
cheese = 0
for i in range(n):
    arr = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    cheese+= sum(arr)
    graph.append(arr)
t = 0
while True:
    if cheese ==0:
        print(t)
        break
    ch = BFS()
    for i in range(n):
        for j in range(m):
            if ch[i][j]>=2:
                cheese-=1
                graph[i][j] = 0
    t+=1