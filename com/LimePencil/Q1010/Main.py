import sys
import math

n = int(sys.stdin.readline().rstrip("\n"))
for _ in range(n):
    k,n = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    print(math.comb(n,k))