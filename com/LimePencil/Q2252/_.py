import sys
from collections import deque

def topology_sort(indegree):
    queue = deque()
    for j in range(1,n+1):
        if indegree[j] ==0:
            queue.append(j)
    while queue:
        now = queue.popleft()
        print(now,end=" ")
        for i in graph[now]:
            indegree[i] -=1
            if indegree[i] == 0:
                queue.append(i)
        

n,k = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(k):
    s,e = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    graph[s].append(e)
    indegree[e] +=1
topology_sort(indegree)

