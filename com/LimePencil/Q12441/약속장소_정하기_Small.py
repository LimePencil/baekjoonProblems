# k550706님 도와주러 품
import heapq
for TC in range(int(input())):
    n,p,m=map(int,input().split())
    friend=[[] for _ in range(p+1)]
    graph=[set() for _ in range(n+1)]
    ans=[0 for _ in range(n+1)]
    for i in range(1,p+1):
        start,cost_per_distance=map(int,input().split())
        friend[i].append(start)
        friend[i].append(cost_per_distance)
    for i in range(m):
        roadinfo=list(map(int,input().split()))
        distance_between_cities,number_of_cities_in_the_same_road=roadinfo[0],roadinfo[1]
        for j in range(2,number_of_cities_in_the_same_road+1):
            graph[roadinfo[j]].add((distance_between_cities,roadinfo[j+1]))
            graph[roadinfo[j+1]].add((distance_between_cities,roadinfo[j]))
    for i in range(1,p+1):
        distance = [float('inf') for _ in range(n+1)]
        root=friend[i][0]
        speed=friend[i][1]
        distance[root] = 0
        pq = []
        heapq.heappush(pq,(0,root))
        while pq:
            c_d,node = heapq.heappop(pq)
            if distance[node]<c_d:
                continue
            for d,a_n in graph[node]:
                w_d = c_d + d
                if w_d < distance[a_n]:
                    distance[a_n] = w_d
                    heapq.heappush(pq,(w_d,a_n))
        for i in range(n+1):
            ans[i]=max(distance[i]*speed,ans[i])
    if min(ans[1:])!=float('inf'):
        print("Case #{}: {}".format(TC+1,min(ans[1:])))
    else:
        print("Case #{}: {}".format(TC+1,-1))