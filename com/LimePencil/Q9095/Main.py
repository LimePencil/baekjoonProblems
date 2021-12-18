import sys

def DP(n):
    global count
    if(n==0):
        count +=1
    if(n >= 1):
        DP(n-1)
    if(n >= 2):
        DP(n-2)
    if(n>=3):
        DP(n-3)


t = int(sys.stdin.readline().rstrip("\n"))
for _ in range(t):
    n = int(sys.stdin.readline().rstrip("\n"))
    count = 0
    DP(n)
    print(count)
    