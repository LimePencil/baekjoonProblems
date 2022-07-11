import sys

input = sys.stdin.readline
a,b,x,y = list(map(int,input().split()))
if b<a:
    a,b=b,a
if y<x:
    x,y=y,x
print(min(b-a,abs(x-a)+abs(y-b)))