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

t = int(sys.stdin.readline().rstrip("\n"))
for _ in range(t):
    n,k = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    indegree = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    time_for_each_building = [0]+ list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    for _ in range(k):
        s,e = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
        graph[s].append(e)
        indegree[e] +=1
    building_to_win = int(sys.stdin.readline().rstrip("\n"))
    time_taken = topology_sort(indegree)
    print(time_taken[building_to_win])
