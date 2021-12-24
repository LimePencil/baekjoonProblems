import sys

a, b =list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
print(a**2 - b**2)