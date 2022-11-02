import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
dp=[[0]*3 for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(3):
        dp[i][j]=dp[i-1][j]
    s=input()
    if s=="H":
        dp[i][0]+=1
    elif s=="P":
        dp[i][1]+=1
    else:
        dp[i][2]+=1
# first item in split[x] = section before switching, second item= section after switching
m=0
split=[[0,dp[n][i]] for i in range(3)]
for i in range(1,n+1):
    for j in range(3):
        split[j][0]+=dp[i][j]-dp[i-1][j]
        split[j][1]-=dp[i][j]-dp[i-1][j]
    a=max([split[k][0] for k in range(3)])
    b=max([split[k][1] for k in range(3)])
    m=max(m,a+b)
print(m)