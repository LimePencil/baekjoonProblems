import sys
from collections import deque

def topology_sort(indegree):
    queue = deque()
    time_until_that_task = [0]*(n+1)
    for i in range(1,n+1):
        if indegree[i] ==0:
            queue.append(i)
            time_until_that_task[i] = time_for_task[i]
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            indegree[i] -=1
            time_until_that_task[i] = max(time_until_that_task[i],time_for_task[i]+time_until_that_task[now])
            if indegree[i] == 0:
                queue.append(i)
    return time_until_that_task


n = int(sys.stdin.readline().rstrip("\n"))
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
time_for_task = [0]*(n+1)
for i in range(1,n+1):
    ls = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    time_for_task[i] = ls[0]
    for j in range(2,len(ls)):
        graph[ls[j]].append(i)
        indegree[i] +=1
time_taken = topology_sort(indegree)
print(max(time_taken))
