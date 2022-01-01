import sys
from collections import deque

n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
arr = []
for _ in range(n):
    l = []
    e = sys.stdin.readline().rstrip("\n")
    for ch in e:
        l.append(int(ch))
    arr.append(l)

queue = deque()
queue.append([0,0,1])
shortest = 0
visited = [[False for i in range(m)] for j in range(n)]
while queue:
    a,b,c = queue.popleft()
    if (a == n-1 and b == m-1):
        shortest = c
        break
    else:
        if not visited[a][b]:
            visited[a][b] = True
            if(a-1>=0 and arr[a-1][b] ==1):
                queue.append([a-1,b,c+1])
            if(b-1>=0 and arr[a][b-1] ==1):
                queue.append([a,b-1,c+1])
            if(a+1<n and arr[a+1][b] ==1):
                queue.append([a+1,b,c+1])
            if(b+1<m and arr[a][b+1] ==1):
                queue.append([a,b+1,c+1])
print(shortest)