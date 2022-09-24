import sys

input = lambda: sys.stdin.readline().rstrip() 
ans = 0
for _ in range(int(input())):
    a,d,g=list(map(int,input().split()))
    ans=max(2*a*(d+g) if a==d+g else a*(d+g),ans)
print(ans)