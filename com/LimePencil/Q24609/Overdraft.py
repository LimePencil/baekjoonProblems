import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr = [int(input()) for _ in range(n)]
ans=0
m=0
for i in range(n):
    ans+=arr[i]
    m=min(ans,m)
print(m*-1)