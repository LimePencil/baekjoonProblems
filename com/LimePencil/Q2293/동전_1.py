import sys

input = sys.stdin.readline
n,k = list(map(int,input().split(" ")))
arr = []
for _ in range(n):
    arr.append(int(input()))
dp = [0]*(k+1)
dp[0]=1
for j in arr:
    for i in range(1,k+1):
        if i>=j:
            dp[i]+=dp[i-j]
print(dp[k])