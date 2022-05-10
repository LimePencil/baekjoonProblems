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
for _ in range(int(input())):
    n=int(input())
    islands=[]
    
    for _ in range(n):
        x,y= list(map(int,input().split()))
        islands.append([x,y])
    islands.sort(key=lambda x: (x[0],-x[1]))
    temp=sorted(list(set([islands[i][1] for i in range(n)])),reverse=True)
    d={temp[i]:i for i in range(len(temp))}
    for i in range(n):
        islands[i][1]=d[islands[i][1]]
    n=len(temp)
    tree = [0]*(n+1)
    ans=0
    for x,y in islands:
        ans+=query(y+1)
        update(y+1,1)
    print(ans)