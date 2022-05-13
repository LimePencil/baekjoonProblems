import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
s=0
ans=[]
for i in range(1,n+1):
    
    s=arr[i-1]

print(*ans)
