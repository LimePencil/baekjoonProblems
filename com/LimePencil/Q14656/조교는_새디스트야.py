import sys

input = sys.stdin.readline
n = int(input())
cnt=0
arr = list(map(int,input().split()))
for i in range(1,n+1):
    if arr[i-1]!=i:
        cnt+=1

print(cnt)