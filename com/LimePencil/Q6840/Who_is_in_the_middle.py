import sys

input = lambda: sys.stdin.readline().rstrip()
_,b,_ = sorted([int(input()) for _ in range(3)])
print(b)