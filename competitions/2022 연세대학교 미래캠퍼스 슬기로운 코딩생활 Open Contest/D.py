import sys
from collections import deque

def BFS():
    queue = deque()
    queue.append((loc_x,loc_y,0))
    shortest = -1
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[loc_x][loc_y]=True
    dir=[(0,1),(0,-1),(1,0),(-1,0)]
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
for i in range(n):
    for j in range(m):
        if department_store[i][j]==3:
            for a in range(-k,k+1,1):
                for b in range(-(k-abs(a)),(k-abs(a))+1,1):
                    new_x=a+i
                    new_y=b+j
                    if 0<=new_x<n and 0<=new_y<m:
                        if department_store[new_x][new_y]==4:
                            loc_x=new_x
                            loc_y=new_y
                            continue
                        if department_store[new_x][new_y]==0 or department_store[new_x][new_y]==2:
                            department_store[new_x][new_y]=1
        elif department_store[i][j]==4:
            loc_x=i
            loc_y=j
print(BFS())