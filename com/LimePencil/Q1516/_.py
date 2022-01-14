import sys
from collections import deque

def topology_sort(indegree):
    queue = deque()
    time_until_that_building = [0]*(n+1)
    for i in range(1,n+1):
        if indegree[i] ==0:
            queue.append(i)
            time_until_that_building[i] = time_for_each_building[i]
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            indegree[i] -=1
            time_until_that_building[i] = max(time_until_that_building[i],time_for_each_building[i]+time_until_that_building[now])
            if indegree[i] == 0:
                queue.append(i)
    return time_until_that_building

n = int(sys.stdin.readline().rstrip("\n"))
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
time_for_each_building = [0]*(n+1)
for i in range(1,n+1):
    prev_buildings = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    for k,j in enumerate(prev_buildings):
        if k == 0:
            time_for_each_building[i] = j
            continue
        if j != -1:
            graph[j].append(i)
            indegree[i] +=1
            
time_taken = topology_sort(indegree)
print("\n".join(map(str,time_taken[1:])))