import sys
from collections import deque

def topology_sort(indegree):
    queue = deque()
    strahler = [[1,0] for _ in range(m+1)]
    for j in range(1,m+1):
        if indegree[j] ==0:
            queue.append(j)
    while queue:
        now = queue.popleft()
        if strahler[now][1]>= 2:
            strahler[now][0] +=1
        for i in graph[now]:
            indegree[i] -=1
            if strahler[i][0] < strahler[now][0]:
                strahler[i][0] = strahler[now][0]
                strahler[i][1] = 1
            elif strahler[i][0] == strahler[now][0]:
                strahler[i][1] += 1
            if indegree[i] == 0:
                queue.append(i)
    maximum = -1
    for i in range(1,m+1):
        maximum = max(strahler[i][0],maximum)
    return maximum
        
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    test,m,p = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    indegree = [0]*(m+1)
    graph = [[] for _ in range(m+1)]
    for _ in range(p):
        s,e = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
        graph[s].append(e)
        indegree[e] +=1
    sea = topology_sort(indegree)
    print(str(test) + " "+str(sea))