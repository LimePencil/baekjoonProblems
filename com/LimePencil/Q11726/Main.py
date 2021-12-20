import sys

def dp(n):
    global mem
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        if mem[n] ==0:
            mem[n] = dp(n-1) + dp(n-2)
            return mem[n]
        else:
            return mem[n]

sys.setrecursionlimit(2*10**3)
n = int(sys.stdin.readline().rstrip("\n"))
mem = [0]*(n+1)
ans = dp(n)
print(ans%10007)