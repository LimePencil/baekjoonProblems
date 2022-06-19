import sys

input = sys.stdin.readline
k,n = list(map(int,input().split()))
if n==1:
    print(-1)
else:
    if k%(n-1)==0:
        print(k+k//(n-1))
    else:
        print(k+k//(n-1)+1)