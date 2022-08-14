import sys

input = sys.stdin.readline
n = int(input())
ans=0
if n%2==0:
    for _ in range(n//2):
        a=int(input())
        b=int(input())
        ans+=b-a
    print(ans)
else:
    print("still running")