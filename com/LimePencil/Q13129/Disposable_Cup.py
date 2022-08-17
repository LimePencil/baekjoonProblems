import sys

input = sys.stdin.readline
a,b,n = list(map(int,input().split()))
print(*range(b+a*n,b*n+a*n+1,b))