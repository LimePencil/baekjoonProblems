import sys


input = sys.stdin.readline

n = int(input())
arr = [input().rstrip() for _ in range(n)]
cnt=2
for i in range(1,n):
    if arr[i]!=arr[i-1]:
        cnt+=1
print(cnt)