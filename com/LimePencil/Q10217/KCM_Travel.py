import sys

input = sys.stdin.readline
t= int(input())
for _ in range(t):
    n,m,k = list(map(int,input().split(" ")))
    graph = [[]for _ in range(n+1)]
    for _ in range(k):
        u,v,c,d = list(map(int,input().split(" ")))
        graph[u].append((v,c,d))
    dp = [[float('inf') for _ in range(m+1)] for _ in range(n+1)]
    dp[1][0] = 0
    for j in range(m+1):
        for i in range(1,n+1):
            if dp[i][j] == float('inf'):
                continue
            tt = dp[i][j]
            for v,c,d in graph[i]:
                if c+j >m:
                    continue
                dp[v][c+j] = min(dp[v][c+j],tt+d)
    a = min(dp[n])
    if a == float("inf"):
        print("Poor KCM")
    else:
        print(a)