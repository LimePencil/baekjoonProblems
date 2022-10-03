import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
p = int(input())
ans=p
if n>=5:
    ans=min(max(p-500,0),ans)
if n>=10:
    ans=min(max(p//100*90,0),ans)
if n>=15:
    ans=min(max(p-2000,0),ans)
if n>=20:
    ans=min(max(p//100*75,0),ans)
print(ans)