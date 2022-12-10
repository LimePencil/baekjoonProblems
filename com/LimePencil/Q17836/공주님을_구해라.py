import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def BFS():
    time_to_princess=float('inf')
    time_to_sword_then_princess=float('inf')
    q=deque()
    q.append((0,0,0))
    d=[(1,0),(0,1),(-1,0),(0,-1)]
    visited=[[False]*m for _ in range(n)]
    while q:
        x,y,time=q.popleft()
        if visited[x][y]:
            continue
        if castle[x][y]==2:
            time_to_sword_then_princess=time+abs(n-x)+abs(m-y)-2
        if x==n-1 and y==m-1:
            time_to_princess=time
        if time_to_princess!=float('inf') and time_to_sword_then_princess!=float('inf'):
            break
        visited[x][y]=True
        for dx,dy in d:
            nx=dx+x
            ny=dy+y
            if 0<=nx<n and 0<=ny<m and castle[nx][ny]!=1:
                q.append((nx,ny,time+1))
    minium=min(time_to_princess,time_to_sword_then_princess)
    if minium>t:
        print("Fail")
    else:
        print(minium)    

n,m,t = list(map(int,input().split()))
castle=[list(map(int,input().split())) for _ in range(n)]
BFS()