import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
cnt=2
prev=2
for i in range(1,n):
    if arr[i]==arr[i-1]:
        cnt+=prev*2
        prev*=2
    else:
        cnt+=2
        prev=2
    if cnt>=100:
        cnt=0
        arr[i]=-1
        prev=0
print(cnt)