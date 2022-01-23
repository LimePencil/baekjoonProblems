import sys

n = int(sys.stdin.readline().rstrip("\n"))
house = []
for _ in range(n):
    house.append(list(map(int,sys.stdin.readline().rstrip("\n").split(" "))))
minimum = float('inf')
for c in range(3):
    dp = [[0 for _ in range(3)] for _ in range(n)]
    for j in range(3):
        if j == c:
            dp[0][j] = house[0][j]
        else:
            dp[0][j] = float('inf')
    for i in range(1,n):
        dp[i][0] = house[i][0] +  min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = house[i][1] +  min(dp[i-1][2], dp[i-1][0])
        dp[i][2] = house[i][2] +  min(dp[i-1][1], dp[i-1][0])
    for i in range(3):
        if i != c:
            minimum = min(minimum,dp[n-1][i])
print(minimum)