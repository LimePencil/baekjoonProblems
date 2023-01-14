import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
for _ in range(n):
    c,p = list(map(int,input().split()))
    print(c,p)
    print(c*p-2*(c-1))