import sys
import heapq

def bfs():
    pq = []
    heapq.heappush(pq,(0,0,0))
    visited = [[False for _ in range(n)]for _ in range(m)]
    visited[0][0] = True
    while pq:
        d,x,y= heapq.heappop(pq)
        if x == m-1 and y == n-1:
            return d
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0<=a<m and 0<=b<n and visited[a][b] == False:
                heapq.heappush(pq,(d+graph[a][b],a,b))
                visited[a][b] = True
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
graph = []
for _ in range(m):
    line = sys.stdin.readline().rstrip("\n")
    row = []
    for c in line:
        row.append(int(c))
    graph.append(row)
print(bfs())