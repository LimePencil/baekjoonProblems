import sys

input = sys.stdin.readline
a,b = list(map(int,input().split(" ")))
c,d = list(map(int,input().split(" ")))
print(min(b+c,a+d))