import sys
from collections import deque
def DFS(root):
    global visited
    queue = deque()
    queue.append(root)
    visited[root] = 1
    while queue:
        node = queue.popleft()
        for c in graph[node]:
            if visited[c] ==0:
                visited[c] = -visited[node]
                queue.append(c)
            elif visited[c] == visited[node]:
                return False
    return True
    

t= int(sys.stdin.readline().rstrip("\n"))
for _ in range(t):
    v,e = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    graph = [[]for _ in range(v+1)]
    visited = [0 for _ in range(v+1)]
    for _ in range(e):
        a,b= list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
        graph[a].append(b)
        graph[b].append(a)
    divided = True
    for i in range(1,v+1):
        if visited[i] ==0 and not DFS(i):
            divided = False
            break
    
    print("YES" if divided else "NO")