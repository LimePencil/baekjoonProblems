import sys

input = sys.stdin.readline
n = int(input())
ans=0
arr = list(map(int,input().split()))
for a in arr:
    if a==0:
        ans+=2
    else:
        ans+=1/a
print(ans)