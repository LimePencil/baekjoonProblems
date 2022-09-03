import sys

input = sys.stdin.readline
n,m,k = list(map(int,input().split()))
if k<m:
    print((m//k+k-1)*n)
else:
    print(m*n)