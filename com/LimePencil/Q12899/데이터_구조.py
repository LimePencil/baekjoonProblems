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
n=2000000
m=int(input())
tree = [0]*(n+1)

for _ in range(m):
    a,b = list(map(int,input().split(" ")))
    if a ==1:
       update(b,1)
    else:
        l=0
        e=2000000
        while l+1<e:
            mid = (l+e)//2
            if b>query(mid):
                l=mid
            else:
                e=mid
        print(e)
        update(e,-1)