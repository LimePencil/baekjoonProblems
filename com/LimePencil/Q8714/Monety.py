import sys

input = sys.stdin.readline
n = int(input())
s = sum(list(map(int,input().split())))
print(min(n-s,s))