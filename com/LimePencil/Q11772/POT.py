import sys

input = sys.stdin.readline
ans=0
n = int(input())
for _ in range(n):
    s=input().rstrip()
    ans+=int(s[:-1])**int(s[-1])
print(ans)