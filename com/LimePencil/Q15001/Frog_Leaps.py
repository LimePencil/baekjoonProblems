import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr = [int(input()) for _ in range(n)]
ans=0
for i in range(1,n):
    ans+=(arr[i]-arr[i-1])**2
print(ans)