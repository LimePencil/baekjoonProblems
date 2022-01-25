import sys
from collections import deque

def topology_sort(indegree):
    queue = deque()
    ls = [[0 for _ in range(n+1)] for _ in range(n+1)]
    f = [False]*(n+1)
    for j in range(1,n+1):
        if indegree[j] ==0:
            queue.append(j)
            f[j] = True
    last = 0
    while queue:
        now = queue.popleft()
        if f[now]:
            for i,k in graph[now]:
                indegree[i] -=1
                ls[i][now] +=k
                if indegree[i] == 0:
                    queue.append(i)
        else:
            for i,k in graph[now]:
                indegree[i] -=1
                for a in range(1,n+1):
                    ls[i][a] += ls[now][a]*k
                if indegree[i] == 0:
                    queue.append(i)
        last = now
    for i in range(1,n+1):
        if f[i]:
            print(str(i) + " "+ str(ls[last][i]))

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
fundamental = {}
middle = [False]*(n+1)
com = []
for _ in range(m):
    e,s,k = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    com.append((e,s,k))
    graph[s].append((e,k))
    middle[e] =True
    indegree[e] +=1
topology_sort(indegree)