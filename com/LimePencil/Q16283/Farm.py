import sys

input = sys.stdin.readline
a,b,n,w = list(map(int,input().split()))
cnt=0
c=0
d=0
for i in range(1,n):
    j=n-i
    if a*i+b*j==w:
        cnt+=1
        c=i
        d=j
if cnt==1:
    print(c,d)
else:
    print(-1)