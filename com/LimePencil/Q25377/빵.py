import sys

input = sys.stdin.readline
ans=float('inf')
for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    if a>b:
        continue
    else:
        ans=min(ans,b)
print(ans if ans!=float('inf') else -1)
