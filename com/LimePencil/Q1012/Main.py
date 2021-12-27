import sys
from collections import deque

def DFS(loc):
    global land, count,visited, land,m,n
    if visited[loc[0]][loc[1]]:
        return
    stack = deque()
    stack.append(loc)
    while stack:
        a = stack.pop()
        if not visited[a[0]][a[1]]:
            visited[a[0]][a[1]] = True
            c = 0
            if(a[0]-1>=0 and land[a[0]-1][a[1]] ==1):
                stack.append((a[0]-1,a[1]))
            if(a[1]-1>=0 and land[a[0]][a[1]-1] ==1):
                stack.append((a[0],a[1]-1))
            if(a[0]+1<m and land[a[0]+1][a[1]] ==1):
                stack.append((a[0]+1,a[1]))
            if(a[1]+1<n and land[a[0]][a[1]+1] ==1):
                stack.append((a[0],a[1]+1))
    count +=1
            

t = int(sys.stdin.readline().rstrip("\n"))

for _ in range(t):
    m,n,k =  list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    cabbage = []
    land = [[0 for i in range(n)] for j in range(m)]
    visited  = [[False for i in range(n)] for j in range(m)]
    for _ in range(k):
        a =  list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
        cabbage.append(a)
        land[a[0]][a[1]] = 1
    count = 0
    for i in range(k):
        DFS(cabbage[i])
    print(str(count))
        
