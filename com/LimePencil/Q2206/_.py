import sys
from collections import deque

def BFS():
    queue = deque()
    queue.append((0,0,1,False))
    visited = [[[0]*2 for _ in range(m)]for _ in range(n)]
    visited[0][0][0] = 1
    while queue:
        x,y,d,b = queue.popleft()
        if x== n-1 and y == m-1:
            return d
        if 0<=x+1<n and road[x+1][y] ==1 and b==0:
            visited[x+1][y][1] = 1
            queue.append((x+1,y,d+1,1))
        if 0<=x-1<n and road[x-1][y] ==1 and b==0:
            visited[x-1][y][1] = 1
            queue.append((x-1,y,d+1,1))
        if 0<=y+1<m and road[x][y+1] ==1 and b==0:
            visited[x][y+1][1] = 1
            queue.append((x,y+1,d+1,1))
        if 0<=y-1<m and road[x][y-1] ==1 and b==0:
            visited[x][y-1][1] = 1
            queue.append((x,y-1,d+1,1))
        if 0<=x+1<n and road[x+1][y] ==0 and visited[x+1][y][b] == 0:
            visited[x+1][y][b] = 1
            queue.append((x+1,y,d+1,b))
        if 0<=x-1<n and road[x-1][y] ==0 and visited[x-1][y][b] == 0:
            visited[x-1][y][b] = 1
            queue.append((x-1,y,d+1,b))
        if 0<=y+1<m and road[x][y+1] ==0 and visited[x][y+1][b] == 0:
            visited[x][y+1][b] = 1
            queue.append((x,y+1,d+1,b))
        if 0<=y-1<m and road[x][y-1] ==0 and visited[x][y-1][b] == 0:
            visited[x][y-1][b] = 1
            queue.append((x,y-1,d+1,b))
    return -1

n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
road = []
for i in range(n):
    o = sys.stdin.readline().rstrip("\n")
    l = []
    for c in o:
        l.append(int(c))
    road.append(l)
print(BFS())