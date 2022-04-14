import sys
from collections import deque

def topology_sort():
    queue = deque()
    arr=[]
    for j in range(1,n+1):
        if indegree[j] ==0:
            queue.append(j)
    while queue:
        if len(queue)>1:
            return "?"
        now = queue.popleft()
        arr.append(now)
        for i in range(1,n+1):
            if graph[now][i]:
                indegree[i] -=1
                if indegree[i] == 0:
                    queue.append(i)
    if len(arr)!=n:
        return "IMPOSSIBLE"
    else:
        return " ".join(map(str,arr))

input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    graph=[[False]*(n+1) for _ in range(n+1)]
    indegree=[0]*(n+1)
    last=list(map(int,input().split()))
    for i in range(n):
        for j in range(i+1,n):
            indegree[last[j]]+=1
            graph[last[i]][last[j]]=True
    m=int(input())
    for _ in range(m):
        a,b=map(int,input().split())
        if graph[a][b]:
            graph[a][b]=False
            graph[b][a]=True
            indegree[b]-=1
            indegree[a]+=1
        else:
            graph[a][b]=True
            graph[b][a]=False
            indegree[b]+=1
            indegree[a]-=1
    print(topology_sort())