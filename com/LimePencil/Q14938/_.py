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

n,m,r = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
items = [0] + list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
graph = [[]for _ in range(n+1)]
for _ in range(r):
    a,b,w = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    graph[a].append([b,w])
    graph[b].append([a,w])
largest = 0
for i in range(1,n+1):
    dist = dijkrstra(i)
    total = 0
    for k,j in enumerate(dist):
        if j<=m:
            total += items[k]
    largest = max(largest,total)
print(largest)


