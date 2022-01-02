import sys
from collections import deque

n = int(sys.stdin.readline().rstrip("\n"))
arr = []
ones = []
for i in range(n):
    l = []
    e = sys.stdin.readline().rstrip("\n")
    for j,ch in enumerate(e):
        if ch =="1":
            ones.append([i,j])
        l.append(int(ch))

    arr.append(l)
ans = []
visited = [[False for i in range(n)] for j in range(n)]
for o in ones:
    if not visited[o[0]][o[1]]:
        queue = deque()
        queue.append(o)
        shortest = 0
        count = 0
        while queue:
            a,b = queue.popleft()
            if not visited[a][b]:
                count +=1
                visited[a][b] = True
                if(a-1>=0 and arr[a-1][b] ==1):
                    queue.append([a-1,b])
                if(b-1>=0 and arr[a][b-1] ==1):
                    queue.append([a,b-1])
                if(a+1<n and arr[a+1][b] ==1):
                    queue.append([a+1,b])
                if(b+1<n and arr[a][b+1] ==1):
                    queue.append([a,b+1])
        ans.append(count)
print(len(ans))
ans.sort()
for i in ans:
    print(i)
