import sys
import heapq
from collections import deque

def dijkstra(start,end):
    dist = [float('inf') for _ in range(n)]
    dist[start] = 0
    pq = [(0,start)]
    while pq:
        curr_d, node = heapq.heappop(pq)
        if dist[node]<curr_d:
            continue
        for new_node,add_d in enumerate(graph[node]):
            if add_d!=0 and add_d+curr_d < dist[new_node]:
                dist[new_node] = add_d+curr_d
                heapq.heappush(pq,(add_d+curr_d,new_node))
    return dist

def bfs(s,d):
    q = deque()
    q.append(d)
    path_remove = []
    while q:
        node_e = q.popleft()
        if node_e == s:
            continue
        for node_s,di  in enumerate(rgraph[node_e]):
            if node_s != node_e and echeck[node_s][node_e] == True  and di!= 0 and di+distance[node_s]==distance[node_e]:
                path_remove.append((node_s,node_e))
                echeck[node_s][node_e] = False
                q.append(node_s)
    for x,y in path_remove:
        graph[x][y] = 0


input = sys.stdin.readline

while (True):
    arr = list(map(int,input().split(" ")))
    if arr == [0,0]:
        break
    n = arr[0]
    m = arr[1]
    s,d = list(map(int,input().split(" ")))
    graph = [[0 for _ in range(n)] for _ in range(n)]
    rgraph = [[0 for _ in range(n)] for _ in range(n)]
    echeck = [[False for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        u,v,p = list(map(int,input().split(" ")))
        graph[u][v] = p
        rgraph[v][u] = p
        echeck[u][v] = True
    distance = dijkstra(s,d)
    if distance[d] == float('inf'):
        print(-1)
        continue
    bfs(s,d)
    distance = dijkstra(s,d)
    print(distance[d] if distance[d] != float('inf') else -1)
