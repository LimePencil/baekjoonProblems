import sys

input = lambda: sys.stdin.readline().rstrip()
a,b,n = list(map(int,input().split()))
for i in range(n):
    a%=b
    a*=10
print(a//b)