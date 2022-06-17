import math
import sys

input = sys.stdin.readline
n=int(input())
coor=[list(map(int,input().split())) for _ in range(n)]
s=0
for i in range(n):
    s+=int(math.hypot(coor[i][0]-coor[i-1][0],coor[i][1]-coor[i-1][1]))
print(s)