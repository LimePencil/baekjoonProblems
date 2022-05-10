import sys

def update(idx, val,arr):
    while idx <= n:
        arr[idx]+= val
        idx+= (idx&-idx)

def query(idx,arr):
    ans =0
    while idx>0:
        ans+= arr[idx]
        idx-=(idx&-idx)
    return ans

input = sys.stdin.readline
m=int(input())
MOD=1000000007
n = 200001
arr = [int(input()) for _ in range(m)]
tree = [0]*(n+1)
nums = [0]*(n+1)
ans=1
update(arr[0]+1,arr[0],tree)
update(arr[0]+1,1,nums)
for i in range(1,m):
    front= (query(arr[i],nums)*arr[i])-query(arr[i],tree)
    back= (query(n,tree)-query(arr[i]+1,tree))-(query(n,nums)-query(arr[i]+1,nums))*arr[i]
    ans*= front+back
    ans%=MOD
    update(arr[i]+1,arr[i],tree)
    update(arr[i]+1,1,nums)
print(ans%MOD)