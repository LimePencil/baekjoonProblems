import sys
from collections import deque

def move(x,y,dx,dy):
    distance = 0
    while 0<=x+dx<n and 0<=y+dy<m and graph[x+dx][y+dy] !="#" and graph[x][y] !="O":
        x += dx
        y += dy
        distance +=1
    return x,y,distance

def BFS():
    queue = deque()
    visited = [[[[False for _ in range(m)]for _ in range(n)] for _ in range(m)]for _ in range(n)]
    queue.append((red_x,red_y,blue_x,blue_y,1))
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    while queue:
        r1,r2,b1,b2,t = queue.popleft()
        if t >10:
            break
        for i in range(4):
            dx,dy = direction[i]
            rn1,rn2,r_d = move(r1,r2,dx,dy)
            bn1,bn2,b_d = move(b1,b2,dx,dy)
            if graph[bn1][bn2] != "O":
                if graph[rn1][rn2] == "O":
                    print(t)
                    return
                if rn1 == bn1 and rn2 == bn2:
                    if r_d>b_d:
                        rn1-=dx
                        rn2-=dy
                    else:
                        bn1-=dx
                        bn2-=dy
                if not visited[rn1][rn2][bn1][bn2]:
                    visited[rn1][rn2][bn1][bn2] = True
                    queue.append((rn1,rn2,bn1,bn2,t+1))
    print(-1)
        

n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))

red_x = 0
red_y = 0
blue_x = 0
blue_y = 0
hole_x = 0
hole_y = 0
graph = []
for i in range(n):
    arr = list(sys.stdin.readline().rstrip("\n"))
    for j in range(m):
        if arr[j] == "R":
            red_x = i
            red_y = j
        elif arr[j] =="B":
            blue_x = i
            blue_y = j
        elif arr[j] == "O":
            hole_x = i
            hole_y = j
    graph.append(arr)

BFS()