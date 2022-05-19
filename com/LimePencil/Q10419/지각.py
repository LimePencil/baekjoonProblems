import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    ans=0
    for i in range(1,n+1):
        if i+i*i<=n:
            ans=i
        else:
            break
    print(ans)