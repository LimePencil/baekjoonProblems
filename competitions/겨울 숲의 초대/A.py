import sys

input = lambda: sys.stdin.readline().rstrip()
n=int(input())
arr=list(map(int,input().split()))
m=max(arr)
s=sum(arr)
t=0
if m>s-m:
    t+=m
else:
    t+=s//2+s%2
print(-1 if t>1440 else t)
    