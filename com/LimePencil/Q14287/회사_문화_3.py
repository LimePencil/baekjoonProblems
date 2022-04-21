import sys

def dfs(left,right,buhas):
    stack=[(1,0)]
    idx=1
    while stack:
        i,k=stack.pop()
        if left[i]==0:
            left[i]=idx
        if k==len(buhas[i]):
            right[i]=idx
        else:
            idx+=1
            stack.append((i,k+1))
            stack.append((buhas[i][k],0))
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
buhas=[[]for _ in range(n+1)]
tree = [0]*(n+1)
left=[0]*(n+1)
right=[0]*(n+1)
price=[0]*(n+1)
sawons=list(map(int,input().split()))
for i in range(1,n):
    buhas[sawons[i]].append(i+1)
dfs(left,right,buhas)
for _ in range(m):
    l = list(map(int,input().split()))
    if l[0] ==1:
       update(left[l[1]],l[2]) 
    else:
        print(query(right[l[1]])-query(left[l[1]]-1))