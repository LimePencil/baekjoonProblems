import sys
n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
print(n//m)
print(n%m)