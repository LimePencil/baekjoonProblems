import sys

r1, s = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
print(s*2-r1)