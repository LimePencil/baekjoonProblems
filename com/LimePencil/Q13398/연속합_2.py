import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr = list(map(int,input().split()))
dp=[[float('-inf')]*2 for _ in range(n)]
dp[0][0]=arr[0]
m=arr[0]
for i in range(1,n):
    dp[i][0]=max(arr[i],arr[i]+dp[i-1][0])
    dp[i][1]=max(arr[i]+dp[i-1][1],dp[i-1][0])
    m=max(m,dp[i][0],dp[i][1])
print(m)