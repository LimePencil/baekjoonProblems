import sys
import heapq
from collections import deque

def dijkstra(start):
    dist = [float('inf') for _ in range(n+1)]
    path = [0 for _ in range(n+1)]
    dist[start] = 0
    pq = [(0,start)]
    while pq:
        curr_d, node = heapq.heappop(pq)
        if dist[node]<curr_d:
            continue
        for new_node,add_d in graph[node]:
            if  add_d+curr_d < dist[new_node]:
                dist[new_node] = add_d+curr_d
                path[new_node] = node
                heapq.heappush(pq,(add_d+curr_d,new_node))
    return dist, path

input = sys.stdin.readline
n,m = list(map(int,input().split(" ")))
graph = [[]for _ in range(n+1)]
for _ in range(m):
    a,b,c = list(map(int,input().split(" ")))
    graph[a].append((b,c))
    graph[b].append((a,c))
d,p = dijkstra(1)
print(n-1)
for i in range(2,n+1):
    print(p[i],i)