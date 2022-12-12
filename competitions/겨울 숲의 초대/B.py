import sys

input = lambda: sys.stdin.readline().rstrip()
n=int(input())
k,h,q=list(map(int,input().split()))
for _ in range(q):
    a,b=list(map(int,input().split()))
    