import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
l=list(map(int,input().split()))
nums = set(l)
k = int(input())
dp=[float('inf') for _ in range(l[-1]*k+2)]
for i in range(1,l[-1]*k+2):
    if i in nums:
        dp[i]=1
    else:
        for j in range(1,i//2+1):
            dp[i]=min(dp[i],dp[j]+dp[i-j])
    if dp[i]>k:
        s="holsoon" if i%2==0 else "jjaksoon"
        print(f"{s} win at {i}")
        break