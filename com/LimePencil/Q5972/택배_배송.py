import sys
import heapq

def dijkstra(root):
    pq = []
    distance = [float('inf') for _ in range(n+1)]
    pq.append((0,root))
    while pq:
        d,now = heapq.heappop(pq)
        if distance[now]<d:
            continue
        for new_n,new_d in graph[now]:
            if new_d+d<distance[new_n]:
                distance[new_n] = new_d+d
                heapq.heappush(pq,(new_d+d,new_n))
    return distance

input = sys.stdin.readline
n,m = list(map(int,input().split(" ")))
graph = [[]for _ in range(n+1)]
for _ in range(m):
    a,b,c = list(map(int,input().split(" ")))
    graph[a].append((b,c))
    graph[b].append((a,c))
dist = dijkstra(1)
print(dist[n])