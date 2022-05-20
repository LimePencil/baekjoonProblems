import sys

input = sys.stdin.readline

n = int(input())
prev=2
cnt=0
arr = list(map(int,input().split()))
for i in arr:
    if i==0 and prev==2:
        cnt+=1
        prev=i
    elif i==1 and prev==0:
        cnt+=1
        prev=i
    elif i==2 and prev==1:
        cnt+=1
        prev=i
print(cnt)