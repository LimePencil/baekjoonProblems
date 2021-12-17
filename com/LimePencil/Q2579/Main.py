import sys

def dp(n):
    global stair
    if n ==0:
        mem[n] = stair[n]
    elif n == 1:
        mem[n] = stair[n] + stair[n-1]
    elif n == 2:
        mem[n] = max(stair[n]+stair[n-2],stair[n-1]+stair[n])
    elif(mem[n] == 0):
        mem[n] = max(dp(n-2)+stair[n],dp(n-3)+stair[n-1]+stair[n])
    return mem[n]

n = int(sys.stdin.readline().strip("\n"))
stair = []
for _ in range(n):
    stair.append(int(sys.stdin.readline().strip("\n")))
mem = [0]*n
ans = dp(n-1)
sys.stdout.write(str(ans))
