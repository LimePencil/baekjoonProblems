import sys

input = sys.stdin.readline
x=0
y=0
dist=0
for i in range(int(input())):
    if i==0:
        x,y=list(map(int,input().split()))
    else:
        a,b=list(map(int,input().split()))
        dist+=abs(a-x)+abs(b-y)
        x,y=a,b
print(dist)