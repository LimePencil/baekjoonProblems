import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr = list(map(int,input().split()))
cnt=0
for a in arr:
    cnt+=min(n,a)
print(cnt)
