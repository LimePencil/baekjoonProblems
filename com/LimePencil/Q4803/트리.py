import sys
from collections import deque
input = sys.stdin.readline

def BFS(root):
    queue=deque()
    queue.append(root)
    ans = True
    while queue:
        node = queue.popleft()
        if visited[node]:
            ans= False
        for next in table[node]:
            if not visited[next]:
                queue.append(next)
        visited[node]= True
    return ans

t=1
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    table = [[]for _ in range(n+1)]
    visited = [False]*(n+1)
    for _ in range(m):
        a,b=map(int,input().split())
        table[a].append(b)
        table[b].append(a)
    trees = 0
    for i in range(1,n+1):
        if visited[i]:
            continue
        a = BFS(i)
        if a:
            trees+=1
    if trees ==0:
        print("Case {}: No trees.".format(t))
    elif trees==1:
        print("Case {}: There is one tree.".format(t))
    else:
        print("Case {}: A forest of {} trees.".format(t,trees))
    t+=1