from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

def BFS():
    q=deque()
    q.append((0,1))
    visited=[False for _ in range(n+1)]
    visited[1]=True
    m=0
    while q:
        dist,node=q.popleft()
        m=max(m,dist)
        for next_node,d in graph[node]:
            if not visited[next_node]:
                visited[next_node]=True
                q.append((dist+d,next_node))
    return m

n = int(input())
graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = list(map(int,input().split()))
    graph[a].append((b,c))
    graph[b].append((a,c))
print(BFS())