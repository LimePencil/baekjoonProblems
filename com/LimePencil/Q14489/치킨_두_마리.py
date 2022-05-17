import sys

input = sys.stdin.readline
s = sum(list(map(int,input().split())))
n = int(input())
if s>=2*n:
    print(s-2*n)
else:
    print(s)