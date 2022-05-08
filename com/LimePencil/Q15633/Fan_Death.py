import sys

input = sys.stdin.readline
n = int(input())
ans=0
for i in range(1,n+1):
    if n%i==0:
        ans+=i
print(5*ans-24)