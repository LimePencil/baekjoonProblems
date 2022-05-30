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

input = sys.stdin.readline 
for _ in range(int(input())):
    v,e=list(map(int,input().split()))
    graph = {}
    for i in range(1,v+1):
        graph[i] = []
    for _ in range(e):
        a,b,c=list(map(int,input().split()))
        graph[a].append((b,c))
        graph[b].append((a,c))
    n=int(input())
    people=list(map(int,input().split()))
    m=float('inf')
    ans=0
    for i in range(1,v+1):
        dist=dijkstra(graph,i)
        s=0
        for p in people:
            s+=dist[p]
        if s<m:
            m=s
            ans=i
    print(ans)
