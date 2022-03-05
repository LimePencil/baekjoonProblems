import sys

input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print(min(a*e,b+d*max(e-c,0)))