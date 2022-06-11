import sys

input = sys.stdin.readline
n,m = list(map(int,input().split()))
arr=list(map(int,input().split()))
ans=1
for a in arr:
    ans*=a
    ans%=m
print(ans)