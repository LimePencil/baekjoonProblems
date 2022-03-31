import sys

input = sys.stdin.readline
n,m = list(map(int,input().split()))
apps = list(map(int,input().split()))
cost = list(map(int,input().split()))
s = sum(cost)
dp=[[0]*(s+1) for _ in range(n)]
for i in range(n):
    for j in range(s+1):
        if j-cost[i]>=0:
            dp[i][j] = max(dp[i][j],dp[i-1][j-cost[i]]+apps[i])
        dp[i][j] = max(dp[i][j], dp[i - 1][j])
for i in range(s+1):
    if dp[n-1][i]>=m:
        print(i)
        break