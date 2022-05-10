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
n = int(input())
arr = list(map(int,input().split()))
tree = [0]*(n+1)
ans=0
for i in range(n):
    ans+=query(n)-query(arr[i])
    update(arr[i],1)
print(ans)