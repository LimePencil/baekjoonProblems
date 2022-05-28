import sys

input = sys.stdin.readline
n,m = list(map(int,input().split()))
for i in range(n):
    print(*list(range(m*i+1,m*(i+1)+1)))