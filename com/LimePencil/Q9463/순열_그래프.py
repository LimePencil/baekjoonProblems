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
for t in range(int(input())):
    n=int(input())
    tree = [0]*(n+1)
    edge=[]
    arr1=list(map(int,input().split()))
    d1={arr1[i-1]:i for i in range(1,n+1)}
    arr2=list(map(int,input().split()))
    d2={arr2[i-1]:i for i in range(1,n+1)}
    for i in range(1,n+1):
        a=d1[i]
        b=d2[i]
        edge.append((a<<32)|b)
    edge.sort()
    ans=0
    for i in range(n-1,-1,-1):
        b=edge[i] & ((1 << 32)-1)
        ans+=query(b-1)
        update(b,1)
    print(ans)