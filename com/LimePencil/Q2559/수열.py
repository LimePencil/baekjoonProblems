import sys

input = sys.stdin.readline
n,k= map(int,input().split())
arr=list(map(int,input().split()))
s=0
m=float('-inf')
for i in range(n):
    if i<k-1:
        s+=arr[i]
    elif i==k-1:
        s+=arr[i]
        m=max(m,s)
    else:
        s+=arr[i]
        s-=arr[i-k]
        m=max(m,s)
print(m)