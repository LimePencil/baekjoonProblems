import sys

input = sys.stdin.readline
a,b = map(int,input().split())
if a>b:
    b,a = a,b
print((b*(b+1)-(a-1)*a)//2)