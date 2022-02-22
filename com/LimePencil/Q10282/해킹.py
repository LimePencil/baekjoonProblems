import sys
import heapq

def dijkstra(root):
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

t = int(sys.stdin.readline())
for _ in range(t):
    n,d,c = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    graph = [[]for _ in range(n+1)]
    for _ in range(d):
        s,e,w = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
        graph[e].append((s,w))
    dists = dijkstra(c)
    m = 0
    num = 0
    for i in range(1,n+1):
        if dists[i] != float('inf'):
            num+=1
            m = max(m,dists[i])
    print(str(num) +" "+ str(m))
