from math import ceil
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n,c=list(map(int,input().split()))
    print(ceil(n/c))