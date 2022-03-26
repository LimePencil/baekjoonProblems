import sys

input = sys.stdin.readline
a,b = list(map(int,input().split()))
c= a+b-(a**2+b**2)**0.5
print(int(c) if float.is_integer(c) else c)