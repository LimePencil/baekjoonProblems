import sys
import heapq

def dijkstra():
    hqs = [[]for _ in range(n+1)]
    pq = [(0,1)]
    hqs[1].append(0)
    while pq:
        d,node = heapq.heappop(pq)
        for node_n,d_n in graph[node]:
            new_d = d_n+d
            if len(hqs[node_n]) <k:
                heapq.heappush(hqs[node_n],-new_d)
                heapq.heappush(pq,(new_d,node_n))
            elif -(hqs[node_n][0])> new_d:
                heapq.heappop(hqs[node_n])
                heapq.heappush(hqs[node_n],-new_d)
                heapq.heappush(pq,(new_d,node_n))
    return hqs


input = sys.stdin.readline
n,m,k = list(map(int,input().split(" ")))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = list(map(int,input().split(" ")))
    graph[a].append((b,c))
h =dijkstra()
for i in range(1,n+1):
    if len(h[i])<k:
        print(-1)
    else:
        print(-heapq.heappop(h[i]))