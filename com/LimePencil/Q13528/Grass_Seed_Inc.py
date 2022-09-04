import sys

input = sys.stdin.readline
c = float(input())
n = int(input())
ans=0
for _ in range(n):
    w,l=list(map(float,input().split()))
    ans+=w*l*c
print(ans)