import sys

input = lambda: sys.stdin.readline().rstrip()
q,n,d= list(map(int,input().split()))
f1=list(input())
f2=list(input())
dp=[[0]*(d+1) for _ in range(n+1)]
for i in range(1,n+1):
    if i==1:
        if f1[i-1]==f2[i-1]:
            dp[i][0]=1
            dp[i][1]=0
            if d>=2:
                dp[i][2]=q-1
        else:
            dp[i][0]=0
            dp[i][1]=2
            if d>=2:
                dp[i][2]=q-2
        continue
    for j in range(d+1):
        if f1[i-1]==f2[i-1]:
            dp[i][j]+=dp[i-1][j]
            if j>=2:
                dp[i][j]+=(q-1)*dp[i-1][j-2]
        else:
            if j>=1:
                dp[i][j]+=2*dp[i-1][j-1]
            if j>=2:
                dp[i][j]+=(q-2)*dp[i-1][j-2]
print(dp[n][d])