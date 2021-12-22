import sys
from collections import deque

def BFS(s):
    global queue, ans, distance, k, found, found_dist
    
    queue.append(s)
    while queue:
        s = queue.popleft()
        if found and  s==k and distance[s] == found_dist:
            ans.append(distance[s])
        elif(s == k and not found):
            ans.append(distance[s])
            found = True
            found_dist = distance[s]
        if not found:
            for i in (s-1,s+1):
                if 0<= i <= 100000 and (distance[i] == 0 or distance[i] ==distance[s]+1):
                    queue.append(i)
                    distance[i] = distance[s] +1
            


n, k =list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
queue = deque()
ans = []
found = False
found_dist = 0
distance = [0]*(100001)
BFS(n)
print(str(found_dist)+"\n"+str(len(ans)))