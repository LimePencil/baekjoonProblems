import sys

input = lambda: sys.stdin.readline().rstrip()
h,m = list(map(int,input().split()))
t=60*h+m
print(t-60*9)