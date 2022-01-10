import sys
import heapq

def dijkstra(graph, start):
    distances = {i:float('inf') for i in graph}
    distances[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        d,n = heapq.heappop(q)
        if distances[n] < d:
            continue
        for n_new,d_new in graph[n]:
            total_dist = d_new + d
            if total_dist < distances[n_new]:
                distances[n_new] = total_dist
                heapq.heappush(q,(total_dist,n_new))
    return distances

v,e = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
graph = {}
start = int(sys.stdin.readline().rstrip("\n"))
for i in range(1,v+1):
    graph[i] = []
for _ in range(e):
    s,e,w = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    graph[s].append((e,w))
dists = dijkstra(graph,start)
for i in range(1,v+1):
    num = dists[i]
    if num == float('inf'):
        print("INF")
    else:
        print(num)
