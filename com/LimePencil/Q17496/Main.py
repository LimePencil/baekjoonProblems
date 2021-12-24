import sys

n, t, c, p = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))

print((n-1)//t*c*p)