import sys


def rangeXOR(n) :
    if n % 4 == 0 :
        return n
    if n % 4 == 1 :
        return 1
    if n % 4 == 2 :
        return n + 1
    return 0

input = lambda: sys.stdin.readline().rstrip()
n = int(input())

c=0
for _ in range(n):
    x,m=map(int,input().split())
    c^=rangeXOR(m+x-1)^rangeXOR(x-1)
if c!=0:
    print("koosaga")
else:
    print("cubelover")