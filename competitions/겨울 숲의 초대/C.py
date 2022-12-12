import sys

input = lambda: sys.stdin.readline().rstrip()
n=int(input())
ans=0
for i in range(1,n+1):
    ans+=n/i
print(ans)