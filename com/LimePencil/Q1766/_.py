import heapq
import sys
import heapq

def topology_sort(indegree):
    p_queue = []
    for j in range(1,n+1):
        if indegree[j] ==0:
            heapq.heappush(p_queue,j)
    while p_queue:
        now = heapq.heappop(p_queue)
        print(now,end=" ")
        for i in graph[now]:
            indegree[i] -=1
            if indegree[i] == 0:
                heapq.heappush(p_queue,i)
        

n,k = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(k):
    s,e = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    graph[s].append(e)
    indegree[e] +=1
topology_sort(indegree)