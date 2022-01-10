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

        
if n != 1:
    graph = [0]*(n+1)
    for _ in range(n-1):
        p,s,w=list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
        if graph[p] == 0:
            graph[p] = [(s,w)]
        else:
            graph[p].append((s,w))
        if graph[s] == 0:
            graph[s] = [(p,w)]
        else:
            graph[s].append((p,w))
    mn,md = DFS(1,n)
    mn, md = DFS(mn,n)
    print(md)
else:
    print("0")