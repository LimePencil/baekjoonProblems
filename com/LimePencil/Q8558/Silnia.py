import sys

input = sys.stdin.readline
n = int(input())
ans=1
for i in range(1,n+1):
    ans*=i
    ans%=10
print(ans)