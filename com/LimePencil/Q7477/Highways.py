import sys

input = sys.stdin.readline
n = int(input())
dist=[0]+list(map(int,input().split()))
if n<4:
    print(0)
else:
    m=float('inf')
    a=0
    b=0
    for i in range(1,n-2):
        if dist[i+1]-dist[i]<m:
            m=dist[i+1]-dist[i]
            a=i+2
            b=i+1
    print(m+dist[-1])
    print(a,1,n,b)