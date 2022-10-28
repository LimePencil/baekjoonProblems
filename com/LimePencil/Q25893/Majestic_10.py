import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
for _ in range(n):
    l=list(map(int,input().split()))
    a,b,c=sorted(l)
    ans="zilch"
    if a>=10:
        ans="triple-double"
    elif b>=10:
        ans="double-double"
    elif c>=10:
        ans="double"
    print(*l)
    print(ans)
    print()
