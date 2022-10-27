import sys

input = lambda: sys.stdin.readline().rstrip()
a,b = list(map(int,input().split()))
n = int(input())
for _ in range(n):
    c=int(input())
    print(c,a*min(1000,c)+b*max(c-1000,0))