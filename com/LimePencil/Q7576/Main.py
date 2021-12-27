import sys
from collections import deque

def BFS(pos):
    global visited,land,n,m,max_days,ripe
    queue = deque(pos)
    l = len(pos)
    first = True
    while queue:
        a = queue.popleft()
        if not visited[a[0]][a[1]]:
            visited[a[0]][a[1]] = True
            if(land[a[0]][a[1]] == 0):
                ripe +=1
            land[a[0]][a[1]]  = 1
            count = 0
            if(a[0]-1>=0 and land[a[0]-1][a[1]] ==0):
                queue.append((a[0]-1,a[1],a[2]+1))
                count +=1
            if(a[1]-1>=0 and land[a[0]][a[1]-1] ==0):
                queue.append((a[0],a[1]-1,a[2]+1))
                count +=1
            if(a[0]+1<m and land[a[0]+1][a[1]] ==0):
                queue.append((a[0]+1,a[1],a[2]+1))
                count +=1
            if(a[1]+1<n and land[a[0]][a[1]+1] ==0):
                queue.append((a[0],a[1]+1,a[2]+1))
                count +=1
            if(count ==0):
                max_days = max(max_days,a[2])
n, m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))

land = []

for _ in range(m):
    land.append(list(map(int,sys.stdin.readline().rstrip("\n").split(" "))))

loc = []
max_days = 0
target = 0
ripe = 0
visited = [[False for i in range(n)] for j in range(m)]
for i in range(m):
    for j in range(n):
        if land[i][j] == 0:
            target +=1
        if(land[i][j] == 1):
            loc.append((i,j,0))
BFS(loc)

if target != ripe:
    print("-1")
else:
    print(max_days)
