import sys

input = sys.stdin.readline
x,y = list(map(int,input().split()))
pos=x
z=y-x
d=1
dist=0
while True:
    if (d>0 and abs(z)>abs(d)) or (d>0 and z<0) or (d<0 and abs(z)>abs(d)) or (d<0 and z>0):
        dist+=abs(x+d-pos)
        pos=x+d
        d*=-2
    else:
        dist+=abs(y-pos)
        break
print(dist)