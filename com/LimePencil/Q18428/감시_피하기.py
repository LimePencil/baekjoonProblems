from itertools import combinations
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
location=[]
teacher=[]
empty=[]
for i in range(n):
    arr = input().split()
    for j in range(n):
        if arr[j]=="T":
            teacher.append((i,j))
        elif arr[j]=="X":
            empty.append((i,j))
    location.append(arr)
comb=combinations(empty,3)
d=[(1,0),(-1,0),(0,1),(0,-1)]
for obstacle in comb:
    for x,y in obstacle:
        location[x][y]="O"
    caught=False
    for x,y in teacher:
        for dx,dy in d:
            for i in range(1,n):
                nx=x+dx*i
                ny=y+dy*i
                if 0<=nx<n and 0<=ny<n and location[nx][ny]!="O":
                    if location[nx][ny]=="S":
                        caught=True
                else:
                    break
                if caught:
                    break
        if caught:
            break
    if not caught:
        print("YES")
        break
    for x,y in obstacle:
        location[x][y]="X"
else:
    print("NO")