import sys

input = sys.stdin.readline
l,r,a = list(map(int,input().split()))
while a!=0:
    if l<=r:
        l+=1
    else:
        r+=1
    a-=1
print(min(l,r)*2)