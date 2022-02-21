import sys

input = sys.stdin.readline
n,k = list(map(int,input().split(" ")))
arr = list(map(int,input().split(" ")))
dp = [0]*(n)
dp[0] = arr[0]
for i in range(1,n):
    dp[i] = dp[i-1]+arr[i]
m =0
for i in range(n):
    if i+k <n:
        m = max(m,dp[i+k] - dp[i])
    else:
        m = max(m,dp[(i+k)%n] - dp[i]+dp[n-1])
print(m)