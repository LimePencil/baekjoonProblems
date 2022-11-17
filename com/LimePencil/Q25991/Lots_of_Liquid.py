import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr = list(map(float,input().split()))
ans=0
for a in arr:
    ans+=a**3
print(ans**(1/3))