import sys
from collections import deque


n = int(sys.stdin.readline().rstrip("\n"))
arr = []
visited = [[False]*n for _ in range(n)]
shark = None
for i in range(n):
    l = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    arr.append(l)
    for j,k in enumerate(l):
        if k == 9:
            shark = (i,j,0)
            arr[i][j] = 0
            visited[i][j] = True
size = 2
queue = deque()
queue.append(shark)
ans = 0
possible_moves = [(-1,0),(0,-1),(0,1),(1,0)]
ate = 0
fishes = []
while True:
    while queue:
        x,y, moves = queue.popleft()
        for dx,dy in possible_moves:
            if 0<=(x+dx)<n and 0<=(y+dy)<n and arr[x+dx][y+dy] <= size and visited[x+dx][y+dy] == False:
                queue.append((x+dx,y+dy,moves+1))
                visited[x+dx][y+dy] = True
                if 0<arr[x+dx][y+dy]<size:
                    fishes.append((x+dx,y+dy,moves+1))
    if len(fishes) != 0:
        fishes.sort(key=lambda x:(x[2],x[0],x[1]))
        queue.append(fishes[0])
        arr[fishes[0][0]][fishes[0][1]] = 0
        ans = fishes[0][2]
        ate+=1
        if ate == size:
            size +=1
            ate = 0
        visited = [[False]*n for _ in range(n)]
        visited[fishes[0][0]][fishes[0][1]] = True
        fishes = []
    else:
        # call mom
        break
print(ans)