import sys
from collections import deque

def DFS():
    global count
    stack = deque()
    # 0 가로 1 세로 2 대각선
    stack.append((0,1,0))
    while stack:
        x,y,o = stack.pop()
        if x == n-1 and y ==n-1:
            count +=1
            continue
        if o ==0:
            if 0<=x<n and 0<=y+1<n and graph[x][y+1]!=1:
                stack.append((x,y+1,0))
            if 0<=x+1<n and 0<=y+1<n and graph[x+1][y+1]!=1 and graph[x][y+1]!=1 and graph[x+1][y]!=1:
                stack.append((x+1,y+1,2))
        elif o==1:
            if 0<=x+1<n and 0<=y<n and graph[x+1][y]!=1:
                stack.append((x+1,y,1))
            if 0<=x+1<n and 0<=y+1<n and graph[x+1][y+1]!=1 and graph[x][y+1]!=1 and graph[x+1][y]!=1:
                stack.append((x+1,y+1,2))
        else:   
            if 0<=x<n and 0<=y+1<n and graph[x][y+1]!=1:
                stack.append((x,y+1,0))
            if 0<=x+1<n and 0<=y<n and graph[x+1][y]!=1:
                stack.append((x+1,y,1))
            if 0<=x+1<n and 0<=y+1<n and graph[x+1][y+1]!=1 and graph[x][y+1]!=1 and graph[x+1][y]!=1:
                stack.append((x+1,y+1,2))

n = int(sys.stdin.readline().rstrip("\n"))

graph = []
count = 0
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip("\n").split(" "))))
DFS()
print(count)