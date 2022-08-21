import sys

input = sys.stdin.readline
n,k = list(map(int,input().split()))
arr=[int(input()) for _ in range(n)]
gift=0
for i in range(1,n):
    if arr[i-1]-arr[i]>=k:
        gift+=1
print(gift)