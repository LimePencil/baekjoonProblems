import sys

input = sys.stdin.readline
ans=5000
arr = list(map(int,input().split()))
for a in arr:
    if a==1:
        ans-=500
    elif a==2:
        ans-=800
    else:
        ans-=1000
print(ans)