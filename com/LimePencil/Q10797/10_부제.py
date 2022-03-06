import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split(" ")))
cnt = 0
for a in arr:
    if a == n:
        cnt+=1
print(cnt)