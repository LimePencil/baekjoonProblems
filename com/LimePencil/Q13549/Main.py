import sys
from collections import deque

def BFS(s):
    global queue, ans, distance, k, found, found_dist
    
    queue.append(s)
    while queue:
        s = queue.popleft()
        if(s == k):
            ans.append(distance[s])
            found = True
            found_dist = distance[s]
        if not found or distance[s] < found_dist:
            i = s+1
            if 0<= i <= 100000 and (not visited[i]):
                queue.append(i)
                visited[i]= True
                distance[i] = distance[s] +1
            i = s-1
            if 0<= i <= 100000 and (not visited[i]):
                queue.append(i)
                distance[i] = distance[s] +1
                visited[i]= True
            i = 2*s
            if 0< i <= 200000:
                queue.appendleft(i)
                distance[i] = distance[s]
                visited[i]= True
            
            


n, k =list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
queue = deque()
ans = []
found = False
found_dist = 0
distance = [0]*(200001)
visited = [False]*(200001)
BFS(n)
print(found_dist)