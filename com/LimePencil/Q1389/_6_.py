import sys
from collections import deque
n, m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
d = {}
for _ in range(m):
    n1 ,n2 = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    if n1 not in d:
        d[n1] = [n2]
    else:
        d[n1].append(n2)
    if n2 not in d:
        d[n2] = [n1]
    else:
        d[n2].append(n1)
num = float('inf')
ans = 0
for i in range(1,n+1):
    bacon = [0]*(n+1)
    visited = [False]*(n+1)
    queue = deque()
    queue.append((i,1))

    while queue:
        q,depth = queue.popleft()
        visited[q] = True 
        for j in d[q]:
            if not visited[j]:
                bacon[j] = depth
                queue.append((j,depth+1))
    s = sum(bacon)
    if num > s:
        num = s
        ans = i
print(ans)
