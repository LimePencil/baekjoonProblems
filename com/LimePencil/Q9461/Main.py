import sys

for _ in range(int(sys.stdin.readline().rstrip("\n"))):
    n = int(sys.stdin.readline().rstrip("\n"))
    mem = [-1]*(n+1)
    for i in range(1,n+1):
        ans = -1
        if i == 1 or i == 2 or i ==3:
            ans = 1
        else:
            ans = mem[i-3] + mem[i-2]
        mem[i] = ans
    print(mem[n])
