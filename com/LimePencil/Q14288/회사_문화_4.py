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
def update1(idx, val):
    while idx <= n:
        tree_one[idx]+= val
        idx+= (idx&-idx)

def query1(idx):
    ans =0
    while idx>0:
        ans+= tree_one[idx]
        idx-=(idx&-idx)
    return ans
def update2(idx, val):
    while idx <= n:
        tree_two[idx]+= val
        idx+= (idx&-idx)

def query2(idx):
    ans =0
    while idx>0:
        ans+= tree_two[idx]
        idx-=(idx&-idx)
    return ans
input = sys.stdin.readline
n,m = list(map(int,input().split()))
buhas=[[]for _ in range(n+1)]
tree_one = [0]*(n+1)
tree_two = [0]*(n+1)
left=[0]*(n+1)
right=[0]*(n+1)
sawons=list(map(int,input().split()))
for i in range(1,n):
    buhas[sawons[i]].append(i+1)
dfs(left,right,buhas)
to_buha=True
for _ in range(m):
    l = list(map(int,input().split()))
    if l[0] ==1:
        if to_buha==True:
            update2(left[l[1]],l[2])
            update2(right[l[1]]+1,-l[2])
        else:
            update1(left[l[1]],l[2]) 
    elif l[0]==2:
        print(query1(right[l[1]])-query1(left[l[1]]-1)+query2(left[l[1]]))
    else:
        to_buha= not to_buha