import sys

n, m = list(map(int,sys.stdin.readline().strip("\n").split(" ")))
coins = []
ans = 0
for i in range(n):
    coins.append(int(sys.stdin.readline().strip("\n")))
for j in reversed(coins):
    a = m//j
    m -= j*a
    ans += a
sys.stdout.write(str(ans))