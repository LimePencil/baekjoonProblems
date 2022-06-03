import sys

input=sys.stdin.readline
n = int(input())
p= [list(map(int,input().split())) for _ in range(n)]
m = int(input())
for _ in range(m):
    x1,y1,z1,r1=list(map(int,input().split()))
    r1*=r1
    s=0
    for x2,y2,z2 in p:
        r2=(x1-x2)**2+(y1-y2)**2+(z1-z2)**2
        if r1>=r2:
            s+=1
    print(s)