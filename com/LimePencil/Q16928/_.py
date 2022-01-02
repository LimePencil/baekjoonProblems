import sys
from collections import deque

ladder, snake = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
queue = deque()
route = list(range(101))
visited = [False]*101
queue.append((1,0))
for _ in range(ladder+snake):
    s,e =list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    route[s] = e
ans = 0
while queue:
    c,d= queue.popleft()
    
    if c==100:
        ans = d
        break
    elif not visited[c]:
        visited[c] = True
        if c+1<=100:
            queue.append((route[c+1],d+1))
        if c+2<=100:
            queue.append((route[c+2],d+1))
        if c+3<=100:
            queue.append((route[c+3],d+1))
        if c+4<=100:
            queue.append((route[c+4],d+1))
        if c+5<=100:
            queue.append((route[c+5],d+1))
        if c+6<=100:
            queue.append((route[c+6],d+1))
print(ans)

