import math
import sys

input=sys.stdin.readline
n,k=map(int,input().split())
mod=int(1e9+7)
print((pow(2,k-1,mod)%mod*math.comb(n,k)%mod)%mod)