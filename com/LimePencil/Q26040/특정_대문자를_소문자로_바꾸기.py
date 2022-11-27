import sys

input = lambda: sys.stdin.readline().rstrip()
s = input()
arr = input().split()
ans=""
for c in s:
    if c in arr:
        ans+=c.lower()
    else:
        ans+=c
print(ans)