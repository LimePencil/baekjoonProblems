import sys
import heapq

def dijkstra():
    pq = []
    heapq.heappush(pq,(graph[0][0],0,0))
    visited = [[False for _ in range(n)]for _ in range(n)]
    visited[0][0] = True
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    while pq:
        d,x,y= heapq.heappop(pq)
        if x == n-1 and y == n-1:
            return d
        for i in range(4):
            dx,dy = direction[i]
            if 0<=x+dx<n and 0<=y+dy<n and not visited[x+dx][y+dy]:
                heapq.heappush(pq,(d+graph[x+dx][y+dy],x+dx,y+dy))
                visited[x+dx][y+dy] = True
t = 0
while n := int(sys.stdin.readline().rstrip("\n")):
    t+=1
    graph = []
    ans = 0
    for _ in range(n):
        graph.append(list(map(int,sys.stdin.readline().rstrip("\n").split(" "))))
    ans = dijkstra()

    print("Problem {}: {}".format(t,ans))
