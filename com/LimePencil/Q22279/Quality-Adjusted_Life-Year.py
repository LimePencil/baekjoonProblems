import sys

input = sys.stdin.readline
ans=0
for _ in range(int(input())):
    q,y=list(map(float,input().split()))
    ans+=q*y
print(ans)