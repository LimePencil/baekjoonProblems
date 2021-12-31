import sys
import math
n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
print(math.comb(n,m))