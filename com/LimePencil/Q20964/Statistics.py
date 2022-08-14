import sys

input = sys.stdin.readline
n = int(input())
arr=[int(input()) for _ in range(n)]
ans=0
for i in range(1,n):
    if arr[i-1]<arr[i]:
        ans+=arr[i]-arr[i-1]
        arr[i]=arr[i-1]
print(ans)