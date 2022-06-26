import sys

input = sys.stdin.readline
w,n,_ = list(map(int,input().split()))
punches=list(map(int,input().split()))
ans=0
for p in punches:
    if w<=p<=n:
        ans+=1
print(ans)