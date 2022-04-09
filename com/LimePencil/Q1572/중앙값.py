import sys

def update(idx, val):
    while idx <= n:
        tree[idx]+= val
        idx+= (idx&-idx)

def query(idx):
    ans =0
    while idx>0:
        ans+= tree[idx]
        idx-=(idx&-idx)
    return ans

input = sys.stdin.readline
n=65537
m,k=list(map(int,input().split()))
arr=[int(input()) for _ in range(m)]
tree = [0]*(n+1)
s=0
b=(k+1)//2
for i in range(m):
    if i <k-1:
       update(arr[i]+1,1)
    else:
        update(arr[i]+1,1)
        l=0
        e=n
        while l+1<e:
            mid = (l+e)//2
            if b>query(mid):
                l=mid
            else:
                e=mid
        s+=e-1
        update(arr[i-k+1]+1,-1)
print(s)