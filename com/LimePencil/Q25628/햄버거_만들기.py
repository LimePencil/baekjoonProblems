import sys

input = lambda: sys.stdin.readline().rstrip()
a,b = map(int,input().split())
print(min(a//2,b))