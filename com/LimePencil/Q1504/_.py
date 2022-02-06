import sys
import heapq

def dijkrstra(root):
    distance = [float('inf') for _ in range(n+1)]
    distance[root] = 0
    pq = []
    heapq.heappush(pq,(0,root))
    while pq:
        c_d,node = heapq.heappop(pq)
        if distance[node]<c_d:
            continue
        for a_n,d in graph[node]:
            w_d = c_d + d
            if w_d < distance[a_n]:
                distance[a_n] = w_d
                heapq.heappush(pq,(w_d,a_n))
    return distance

n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
graph = [[]for _ in range(n+1)]
for _ in range(m):
    a,b,w = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    graph[a].append([b,w])
    graph[b].append([a,w])
f,s = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
first_then_second = 0
dist = dijkrstra(1)
first_then_second += dist[f]
dist = dijkrstra(f)
first_then_second += dist[s]
dist = dijkrstra(s)
first_then_second += dist[n]

second_then_first = 0
dist = dijkrstra(1)
second_then_first += dist[s]
dist = dijkrstra(s)
second_then_first += dist[f]
dist = dijkrstra(f)
second_then_first += dist[n]

print(-1 if min(second_then_first,first_then_second) == float('inf') else min(second_then_first,first_then_second))