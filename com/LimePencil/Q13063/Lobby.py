import sys

input = sys.stdin.readline
while True:
    n,m,k=list(map(int,input().split()))
    if n==m==k==0:
        break
    i=n-m-k
    if n//2+1-m<=i:
        print(max(0,n//2+1-m))
    else:
        print(-1)