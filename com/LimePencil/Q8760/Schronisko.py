import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    w,h=list(map(int,input().split()))
    print(w*h//2)