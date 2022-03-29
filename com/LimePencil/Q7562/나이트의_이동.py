import queue
import sys
from collections import deque

def BFS(x,y,x_end,y_end):
    queue = deque()
    queue.append((x,y,0))
    direction = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    visited = [[False]*n for _ in range(n)]
    visited[x][y] = True
    while queue:
        x,y,s = queue.popleft()
        if x==x_end and y==y_end:
            return s
        for dx,dy in direction:
            nx=dx+x
            ny=dy+y
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny,s+1))
input = sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    print(BFS(x1,y1,x2,y2))