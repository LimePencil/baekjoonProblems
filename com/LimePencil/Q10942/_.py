import sys


n = int(sys.stdin.readline().rstrip("\n"))
arr = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
dp = [[0 for _ in range(n)]for _ in range(n)]
for i in range(n):
    for s in range(n):
        e = s+i
        if e>=n:
            break
        if i ==0:
            dp[s][e] = 1
        elif i ==1:
            if arr[s] == arr[e]:
               dp[s][e] = 1
        else:
            if arr[s] == arr[e] and dp[s+1][e-1] == 1:
                dp[s][e] = 1
m = int(sys.stdin.readline().rstrip("\n"))
for _ in range(m):
    s,e = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    print(str(dp[s-1][e-1]))