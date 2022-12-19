import sys

input = lambda: sys.stdin.readline().rstrip()
while (n:=int(input()))!=0:
    print(n*(n+1)//2)