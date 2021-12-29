import sys
import math

n,k = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
print(math.comb(n,k)%10007)