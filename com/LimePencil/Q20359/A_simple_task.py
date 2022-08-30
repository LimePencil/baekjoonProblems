from math import log2
import sys

input = sys.stdin.readline
n = int(input())
cnt=0
while n%2==0:
    n//=2
    cnt+=1
print(n,cnt)