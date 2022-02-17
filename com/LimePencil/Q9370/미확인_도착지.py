import sys
import heapq

def dijkrstra(root):
    distance = [100000000 for _ in range(n+1)]
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

t = int(sys.stdin.readline().rstrip("\n"))
for _ in range(t):
    n,m,x = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    s,g,h = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    graph = [[]for _ in range(n+1)]
    weight = 0
    for _ in range(m):
        a,b,w = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
        graph[a].append([b,w])
        graph[b].append([a,w])
    target = []
    for i in range(x):
        target.append(int(sys.stdin.readline().rstrip("\n")))
    dist_home1 = dijkrstra(s)
    dist_home2 = dijkrstra(h)
    dist_home3 = dijkrstra(g)
    poss_target = []
    minimum = float('inf')
    target.sort()
    for i in target:
        if dist_home1[i] == dist_home1[h]+dist_home2[g]+dist_home3[i] or dist_home1[i] == dist_home1[g]+dist_home3[h]+dist_home2[i]:
            poss_target.append(str(i))
    print(*poss_target)