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
arr = [0] + list(map(int,input().split(" ")))
tree = [0]*(n+1)
for i in range(1,n+1):
    update(i,arr[i])
m=int(input())
ones=[]
twos=[]
for i in range(m):
    var = list(map(int,input().split(" ")))
    a=var[0]
    if a ==1:
       ones.append((var[1],var[2]))
    else:
        twos.append((var[1],var[2],var[3],i))
twos.sort()
index=0
ans=[]
while index<len(twos) and twos[index][0]==0:
    ans.append((twos[index][3],query(twos[index][2])-query(twos[index][1]-1)))
    index+=1
for i in range(len(ones)):
    b,c=ones[i]
    update(b,c-arr[b]) 
    arr[b] = c
    while index<len(twos) and twos[index][0]==i+1:
        ans.append((twos[index][3],query(twos[index][2])-query(twos[index][1]-1)))
        index+=1
ans.sort()
for a,b in ans:
    print(b)
