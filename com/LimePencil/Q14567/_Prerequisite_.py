import sys
from collections import deque

def topology_sort(indegree):
    queue = deque()
    ls = [1]*(n+1)
    for j in range(1,n+1):
        if indegree[j] ==0:
            queue.append((j,1))
    while queue:
        now,index = queue.popleft()
        for i in graph[now]:
            indegree[i] -=1
            ls[i] = index + 1
            if indegree[i] == 0:
                queue.append((i,index+1))
    print(" ".join(map(str,ls[1:])))

n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    graph[s].append(e)
    indegree[e] +=1
topology_sort(indegree)