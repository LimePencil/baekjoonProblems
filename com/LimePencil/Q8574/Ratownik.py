import sys

input = sys.stdin.readline
n,k,x,y = map(int,input().split())
cnt=0
for _ in range(n):
    a,b=map(int,input().split())
    if (x-a)**2+(y-b)**2>k**2:
        cnt+=1
print(cnt)