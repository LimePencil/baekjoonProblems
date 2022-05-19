import sys

input = sys.stdin.readline
n,k= list(map(int,input().split()))
arr=list(map(int,input().split()))
s=0
for i in arr:
    s+=(i-1)//2+1
if s>=n:
    print("YES")
else:
    print("NO")