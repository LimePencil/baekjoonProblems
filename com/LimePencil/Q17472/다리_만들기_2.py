from collections import deque
import sys

def union(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return True
    else:
        root[a]=b
        return False

def find(node):
    if root[node] != node:
        root[node] = find(root[node])
    return root[node]

input = sys.stdin.readline
n,m=map(int,input().split())
dir=[(1,0),(0,1),(-1,0),(0,-1)]
coor=[]

for _ in range(n):
    coor.append(list(map(int,input().split())))

visited=[[False]*m for _ in range(n)]
queue=deque()
kth_island=1
islands=[]
for i in range(n):
    for j in range(m):
        if coor[i][j]==1 and visited[i][j]==False:
            queue.append((i,j))
            coor[i][j]=kth_island
            islands.append((i,j,kth_island))
            visited[i][j]=True
            while queue:
                x,y=queue.popleft()
                for dx,dy in dir:
                    nx=dx+x
                    ny=dy+y
                    if 0<=nx<n and 0<=ny<m:
                        if not visited[nx][ny] and coor[nx][ny]==1:
                            queue.append((nx,ny))
                            coor[nx][ny]=kth_island
                            islands.append((nx,ny,kth_island))
                        visited[nx][ny]=True
            kth_island+=1
kth_island-=1
edges=[]
for x,y,k in islands:
    for dx,dy in dir:
        nx=x
        ny=y
        dist=-1
        while True:
            nx+=dx
            ny+=dy
            dist+=1
            if 0<=nx<n and 0<=ny<m:
                if coor[nx][ny] ==0:
                    continue
                elif coor[nx][ny]!=k:
                    if dist>=2:
                        edges.append((dist,k,coor[nx][ny]))
                        break
                    else:
                        break
                else:
                    break
            else:
                break            

root = list(range(kth_island+1))
nodes=[]
edges.sort()
w=0
count=0
for c,a,b in edges:
    if not union(a,b):
        w+=c
        count+=1
print(w if count==kth_island-1 else -1)