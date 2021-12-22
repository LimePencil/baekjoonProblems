import sys
from collections import deque

def BFS(s):
    global queue, ans, distance, k, route,n
    queue.append(s)
    route[s] = s
    while queue:
        s = queue.popleft()
        
        if(s == k):
            print(distance[s])
            prev = s
            ans.appendleft(s)
            while prev != n:
                prev = route[prev]
                ans.appendleft(prev) 
            print(*ans) 
            break
        for i in (s-1,s+1,2*s):
            if 0<= i <= 100000 and distance[i] == 0:
                queue.append(i)
                route[i] = s
                distance[i] = distance[s] +1


n, k =list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
queue = deque()
ans = deque()
distance = [0]*(100001)
route = [0]*(100001)
BFS(n)