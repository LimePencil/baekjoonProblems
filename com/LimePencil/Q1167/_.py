import sys
from collections import deque

def DFS(node,v):
    stack = deque()
    visited = [False]*(v+1)
    maxdist = 0
    maxnode = 0
    stack.append((node,0))
    visited[node] = True
    while stack:
        n,d = stack.pop()
        for sub in graph[n]:
                n_new, d_new = sub
                d_new += d
                if not visited[n_new]:
                    visited[n] = True
                    if d_new>maxdist:
                        maxdist = d_new
                        maxnode = n_new
                    stack.append((n_new,d_new))
    return maxnode, maxdist

n= int(sys.stdin.readline().rstrip("\n"))
graph = [0]*(n+1)
for _ in range(n):
    l=list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    info = []
    for i in range(1,len(l)-2,2):
        info.append((l[i],l[i+1]))
    graph[l[0]] = info

mn,md = DFS(1,n)
mn, md = DFS(mn,n)
print(md)