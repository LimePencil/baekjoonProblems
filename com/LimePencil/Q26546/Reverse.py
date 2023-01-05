import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
for i in range(n):
    s,a,b=input().split()
    print(s[:int(a)]+s[int(b):])