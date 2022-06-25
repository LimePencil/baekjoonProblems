import sys
from collections import deque

def BFS():
    queue = deque()
    queue.append((loc_x,loc_y,0))
    shortest = -1
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[loc_x][loc_y]=True
    while queue:
        a,b,c = queue.popleft()
        if department_store[a][b]==2:
            shortest = c
            break
        for dx,dy in dir:
            x=dx+a
            y=dy+b
            if 0<=x<n and 0<=y<m and  (department_store[x][y]==0 or department_store[x][y]==2) and not visited[x][y]:
                visited[x][y]=True
                queue.append((x,y,c+1))
    return shortest
                

input=sys.stdin.readline
n,m,k=map(int,input().split())
department_store=[]
loc_x=-1
loc_y=-1
for _ in range(n):
    department_store.append(list(map(int,input().split())))
ma=deque()
dir=[(0,1),(0,-1),(1,0),(-1,0)]
for i in range(n):
    for j in range(m):
        if department_store[i][j]==3:
            ma.append((i,j,0))
        elif department_store[i][j]==4:
            loc_x=i
            loc_y=j
while ma:
    x,y,d=ma.popleft()
    if d>=k:
        continue
    for dx,dy in dir:
        nx=dx+x
        ny=dy+y
        if 0<=nx<n and 0<=ny<m and department_store[nx][ny]!=1:
            ma.append((nx,ny,d+1))
            department_store[nx][ny]=1
print(BFS())