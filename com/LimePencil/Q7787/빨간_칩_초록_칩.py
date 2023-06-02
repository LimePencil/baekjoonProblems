import sys

def get_grundy(n):
    if n&1:
        return 1
    else:
        x=0
        for i in range(30,0,-1):
            if n%(1<<i)==(1<<(i-1)):
                return i

input = lambda: sys.stdin.readline().rstrip()
r,g = list(map(int,input().split()))

print("A player wins" if get_grundy(r)^get_grundy(g) else "B player wins")