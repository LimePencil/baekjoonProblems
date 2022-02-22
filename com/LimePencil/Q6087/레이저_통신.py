import sys
import heapq

def dijkstra(root):
    pq = []
    v = [[float('inf') for _ in range(n+1)]for _ in range(m+1)]

    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    heapq.heappush(pq,(0,root[0][0],root[0][1],-1))
    while pq:
        c_d,x,y,dir = heapq.heappop(pq)
        if x == root[1][0] and y == root[1][1]:
            break
        for i in range(4):
            dx,dy = direction[i]
            n_d = c_d
            if 0<=dx+x<m and 0<=dy+y<n and graph[dx+x][dy+y] !="*":
                if dir != -1 and dir != i:
                    n_d+=1
                if v[dx+x][dy+y] >= n_d:
                    v[dx+x][dy+y] = n_d
                    heapq.heappush(pq,(n_d,dx+x,dy+y,i))
    return v[root[1][0]][root[1][1]]


n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
graph = []
c = []
for i in range(m):
    s = sys.stdin.readline().rstrip("\n")
    graph.append(list(s))
    for j in range(n):
        if s[j] == "C" and len(c) != 2:   
            c.append((i,j))
print(dijkstra(c))