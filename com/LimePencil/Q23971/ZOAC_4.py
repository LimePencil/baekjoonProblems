from math import ceil
import sys

input = sys.stdin.readline
h,w,n,m = list(map(int,input().split()))
print(ceil(h/(n+1))*ceil(w/(m+1)))