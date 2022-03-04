import sys
import heapq

def dijkstra():
    pq = [(0,0,1)]
    distance = [[float('inf') for _ in range(k+1)] for _ in range(n+1)]
    while pq:
        d,count,node = heapq.heappop(pq)
        if distance[node][count] < d:
            continue
        for new_node,weight in graph[node]:
            new_weight= d+weight
            if new_weight<distance[new_node][count]:
                distance[new_node][count] = new_weight
                heapq.heappush(pq,(new_weight,count,new_node))
            if count <k and d< distance[new_node][count+1]:
                distance[new_node][count+1] = d
                heapq.heappush(pq,(d,count+1,new_node))
    print(min(distance[n]))

input = sys.stdin.readline
n,m,k = list(map(int,input().split(" ")))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = list(map(int,input().split(" ")))
    graph[a].append((b,c))
    graph[b].append((a,c))
dijkstra()