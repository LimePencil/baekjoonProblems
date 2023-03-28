import sys

def calculate_cost(a,b):
    if b==0:
        if a==0:
            return 0
        else:
            return 2
    elif abs(a-b)==1 or abs(a-b)==3:
        return 3
    elif abs(a-b)==2:
        return 4
    else:
        return 1

input = lambda: sys.stdin.readline().rstrip()
arr = list(map(int,input().split()))
arr.pop()
dp=[[[float('inf') for _ in range(5)] for _ in range(5)] for _ in range(len(arr)+1)]

dp[0][0][0]=0
for i in range(1,len(arr)+1):
    for j in range(5):
        for k in range(5):
            dp[i][arr[i-1]][j]=min(dp[i][arr[i-1]][j],dp[i-1][k][j]+calculate_cost(arr[i-1],k))
    for k in range(5):
        for j in range(5):
            dp[i][k][arr[i-1]]=min(dp[i][k][arr[i-1]],dp[i-1][k][j]+calculate_cost(arr[i-1],j))
ans=float('inf')
for i in range(5):
    for j in range(5):
        ans=min(ans,dp[len(arr)][i][j])
print(ans)