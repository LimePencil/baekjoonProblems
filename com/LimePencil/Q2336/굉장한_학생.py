import sys
import math

def find_min(node, start, end, left,right):
    if left>end or right<start:
        return float('inf')
    if left<=start and end<=right:
        return tree[node]
    return min(find_min(2*node,start,(start+end)//2,left,right), find_min(2*node+1,(start+end)//2+1,end,left,right))

def change_tree(node, start, end, index,value):
    if index<start or index>end:
        return
    if start== end:
        tree[node] = value
        return
    change_tree(2*node,start,(start+end)//2,index,value)
    change_tree(2*node+1,(start+end)//2+1,end,index,value)
    tree[node] = min(tree[2*node], tree[2*node+1])

input = sys.stdin.readline
n = int(input())
people=[[0]*3 for i in range(n)]
tree = [float('inf')]*2**(math.ceil(math.log2(n))+1)
for i in range(3):
    l=list(map(int,input().split()))
    for j in range(n):
        people[l[j]-1][i]=j
people.sort()
ans=0
for i in range(n):
    m=find_min(1,0,n-1,0,people[i][1])
    if m>people[i][2]:
        ans+=1
    change_tree(1,0,n-1,people[i][1],people[i][2])
print(ans)