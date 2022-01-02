import sys
from collections import deque

n = int(sys.stdin.readline().rstrip("\n"))
arr = []
ones = []
for i in range(n):
    l = []
    e = sys.stdin.readline().rstrip("\n")
    for ch in e:
        l.append(ch)
    arr.append(l)
ans = []
visited = [[False for i in range(n)] for j in range(n)]
count_not_blind = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            queue = deque()
            queue.append([i,j])
            color = arr[i][j]
            while queue:
                a,b = queue.popleft()
                if not visited[a][b]:
                    visited[a][b] = True
                    if(a-1>=0 and arr[a-1][b] == color):
                        queue.append([a-1,b])
                    if(b-1>=0 and arr[a][b-1] == color):
                        queue.append([a,b-1])
                    if(a+1<n and arr[a+1][b] == color):
                        queue.append([a+1,b])
                    if(b+1<n and arr[a][b+1] == color):
                        queue.append([a,b+1])
            count_not_blind+=1

visited = [[False for i in range(n)] for j in range(n)]
count_blind = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            queue = deque()
            queue.append([i,j])
            is_blue = True if arr[i][j] == "B" else False
            while queue:
                a,b = queue.popleft()
                if not visited[a][b]:
                    visited[a][b] = True
                    if(a-1>=0 and is_blue == (True if arr[a-1][b] == "B" else False)):
                        queue.append([a-1,b])
                    if(b-1>=0 and is_blue == (True if arr[a][b-1] == "B" else False)):
                        queue.append([a,b-1])
                    if(a+1<n and is_blue == (True if arr[a+1][b] == "B" else False)):
                        queue.append([a+1,b])
                    if(b+1<n and is_blue == (True if arr[a][b+1] == "B" else False)):
                        queue.append([a,b+1])
            count_blind+=1


print(str(count_not_blind)+" " + str(count_blind))
