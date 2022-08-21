import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    b,p=list(map(float,input().split()))
    print(60*b/p-60/p,60*b/p,60*b/p+60/p)