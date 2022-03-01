import sys
from collections import deque

def BFS(root):
    q = deque()
    q.append(root)
    visited[root] = True
    count =1
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                count +=1
                q.append(next_node)
    return count

input = sys.stdin.readline
n,m = list(map(int,input().split(" ")))
graph = [[]for _ in range(n+1)]
for _ in range(m):
    a,b = list(map(int,input().split(" ")))
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*(n+1)
ans = 1
for i in range(1,n+1):
    if not visited[i]:
        ans*=BFS(i)%1000000007
print(ans%1000000007)