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
price[1]=int(input())
idx=0
for i in range(2,n+1):
    p,x=list(map(int,input().split()))
    price[i]=p
    buhas[x].append(i)
dfs(left,right,buhas)
for i in range(1,n+1):
    range_update(left[i],left[i],price[i])
for _ in range(m):
    l = input().split()
    if l[0] =="p":
       range_update(left[int(l[1])]+1,right[int(l[1])],int(l[2])) 
    else:
        print(query(left[int(l[1])])-query(left[int(l[1])]-1))