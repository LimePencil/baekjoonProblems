# n = int(input())
# L = 1024
# MOD=10007
# dp_table = [[0 for _ in range(10)] for _ in range(L)]
# for i in range(1, 10):
#     dp_table[1<<i][i] = 1
# for i in range(1, n):
#     dp_temp = [[0 for _ in range(10)] for _ in range(L)]
#     for e in range(10):
#         for d in range(L):
#             if e < 9:
#                 dp_temp[d|(1<<e)][e] += dp_table[d][e+1]%MOD
#             if e > 0:
#                 dp_temp[d|(1<<e)][e] += dp_table[d][e-1]%MOD
#     dp_table = dp_temp
# print(sum(dp_table[L-1])%MOD)


n = int(input())

dp = [[1 for i in range(10)] for j in range(n+1)]
for i in range(2,n+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][0:j+1])
print(sum(dp[n])%10007)