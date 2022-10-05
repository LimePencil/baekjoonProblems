import sys

input = lambda: sys.stdin.readline().rstrip()

m = int(input())
n,a,b,c = list(map(int,input().split()))
if m==1:
    print(max(0,a+b+c-2*n))
else:
    print(a)