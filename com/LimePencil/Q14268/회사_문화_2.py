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
def update(idx, val1,val2):
    while idx <= n:
        tree_one[idx]+= val1
        tree_two[idx]+=val2
        idx+= (idx&-idx)

def range_update(left,right,val):
    update(left,val,(-left+1)*val)
    update(right+1,-val,right*val)

def query(idx):
    val1=0
    val2=0
    f=idx
    while idx>0:
        val1+= tree_one[idx]
        val2+= tree_two[idx]
        idx-=(idx&-idx)
    return val1*f+val2
input = sys.stdin.readline
n,m = list(map(int,input().split()))
buhas=[[]for _ in range(n+1)]
tree_one = [0]*(n+1)
tree_two = [0]*(n+1)
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
       range_update(left[l[1]],right[l[1]],l[2]) 
    else:
        print(query(left[l[1]])-query(left[l[1]]-1))