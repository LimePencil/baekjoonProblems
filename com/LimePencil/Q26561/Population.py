import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
for _ in range(n):
    p,t=map(int,input().split())
    p-=t//7-t//4
    print(p)