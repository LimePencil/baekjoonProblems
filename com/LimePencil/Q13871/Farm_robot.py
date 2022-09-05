import sys

input = sys.stdin.readline
n,c,s=list(map(int,input().split()))
arr = list(map(int,input().split()))
curr=0
cnt=0
if s==1:
    cnt+=1
for a in arr:
    curr+=a
    curr%=n
    if curr==s-1:
        cnt+=1
print(cnt)