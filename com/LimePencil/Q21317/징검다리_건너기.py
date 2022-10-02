import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
energy=[list(map(int,input().split())) for _ in range(n-1)]
k= int(input())

dp=[[float('inf')]*2 for _ in range(n+1)]
dp[1][0]=0
for i in range(1,n):
    if i+1<=n:
        dp[i+1][0]=min(dp[i+1][0],dp[i][0]+energy[i-1][0])
        if dp[i][1]!=0:
            dp[i+1][1]=min(dp[i+1][1],dp[i][1]+energy[i-1][0])
    if i+2<=n:
        dp[i+2][0]=min(dp[i+2][0],dp[i][0]+energy[i-1][1])
        if dp[i][1]!=0:
            dp[i+2][1]=min(dp[i+2][1],dp[i][1]+energy[i-1][1])
    if i+3<=n:
        dp[i+3][1]=dp[i][0]+k
print(min(dp[n][:]))