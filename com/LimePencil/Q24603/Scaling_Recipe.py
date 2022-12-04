import sys

input = lambda: sys.stdin.readline().rstrip()
n,x,y = list(map(int,input().split()))
for _ in range(n):
    print(int(input())*y//x)
