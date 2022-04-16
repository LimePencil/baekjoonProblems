import sys
from collections import deque

def BFS():
    count=0
    queue=deque()
    visited=[[False]*(w+2) for _ in range(h+2)]
    direction=[(1,0),(-1,0),(0,1),(0,-1)]
    queue.append((0,0))
    visited[0][0]=True
    while queue:
        x,y=queue.popleft()
        for d in range(4):
            nx=x+direction[d][0]
            ny=y+direction[d][1]
            if nx<0 or nx>h+1 or ny<0 or ny>w+1 or visited[nx][ny] or maps[nx][ny]=="*" or "A"<=maps[nx][ny]<="Z":
                continue
            visited[nx][ny]=True
            queue.append((nx,ny))
            if maps[nx][ny]=="$":
                count+=1
                maps[nx][ny]="."
            elif "a"<=maps[nx][ny]<="z":
                new_key=maps[nx][ny]
                maps[nx][ny]="."
                if maps[nx][ny] not in curr_keys:
                    open_door(new_key)
                    visited=[[False]*(w+2) for _ in range(h+2)]
                    curr_keys.append(new_key)
                    queue=deque()
                    queue.append((nx,ny))
                    visited[nx][ny]=True
                    break
            
    return count

def open_door(key:str):
    key=key.upper()
    for i in range(1,h+1):
        for j in range(1,w+1):
            if maps[i][j]==key:
                maps[i][j]="."
                
input = sys.stdin.readline
for _ in range(int(input())):
    h,w=map(int,input().split())
    maps=[["."]*(w+2) for _ in range(h+2)]
    for i in range(h):
        line=list(input().rstrip("\n"))
        for j in range(w):
            maps[i+1][j+1]=line[j]
    curr_keys=list(input().rstrip("\n"))
    if curr_keys[0]=="0":
        curr_keys=[]
    else:
        for k in curr_keys:
            open_door(k)
    print(BFS())
