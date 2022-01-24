import sys
from collections import deque

def topology_sort(indegree):
    queue = deque()
    for j in range(1,n+1):
        if indegree[j] ==0:
            queue.append(j)
    ans = []
    while queue:
        now = queue.popleft()
        ans.append(str(now))
        for i in graph[now]:
            indegree[i] -=1
            if indegree[i] == 0:
                queue.append(i)
    no_answer = False
    for j in range(1,n+1):
        if indegree[j] !=0:
            no_answer = True
            break
    if no_answer:
        print("0")
    else:
        print("\n".join(ans))
    
        

n,k = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(k):
    ls = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    for i in range(1,len(ls)-1):
        graph[ls[i]].append(ls[i+1])
        indegree[ls[i+1]] +=1
topology_sort(indegree)