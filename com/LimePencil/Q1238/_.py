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

n,m,x = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
graph = [[]for _ in range(n+1)]
for _ in range(m):
    a,b,w = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    graph[a].append([b,w])
dist_home = dijkrstra(x)
farthest = 0
for i in range(1,n+1):
    if i != x:
        dist_come = dijkrstra(i)
        farthest = max(farthest,dist_home[i]+dist_come[x])
print(farthest)