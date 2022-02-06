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

n = int(sys.stdin.readline().rstrip("\n"))
m = int(sys.stdin.readline().rstrip("\n"))
graph = [[]for _ in range(n+1)]
for _ in range(m):
    a,b,w = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    graph[a].append([b,w])
s, e =list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
dist = dijkrstra(s)
print(dist[e])


