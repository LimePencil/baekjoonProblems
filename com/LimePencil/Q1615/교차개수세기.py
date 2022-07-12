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
n,m = list(map(int,input().split()))
tree = [0]*(n+1)
edge=[]
for _ in range(m):
    a,b=map(int,input().split())
    edge.append((a<<32)|b)
edge.sort()
ans=0
for i in range(m-1,-1,-1):
    b=edge[i] & ((1 << 32)-1)
    ans+=query(b-1)
    update(b,1)
print(ans)