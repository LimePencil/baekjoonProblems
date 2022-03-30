import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    cost = [0]+list(map(int,input().split()))
    cumulative_sum = [0]*(n+1)
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        cumulative_sum[i] = cost[i]+cumulative_sum[i-1]
    for i in range(1,n):
        for j in range(1,n-i+1):
            a = i+j
            dp[j][a] = float('inf')
            for k in range(j,a):
                dp[j][a] = min(dp[j][a],dp[j][k]+dp[k+1][a]+cumulative_sum[a]-cumulative_sum[j-1])
    print(dp[1][n])