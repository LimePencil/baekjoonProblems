import sys
import math

def find_sum(node, start, end, left,right):
    if left>end or right<start:
        return 0
    if left<=start and end<=right:
        return tree[node]
    return find_sum(2*node,start,(start+end)//2,left,right) + find_sum(2*node+1,(start+end)//2+1,end,left,right)

def change_tree(node, start, end, index):
    if index<start or index>end:
        return
    if start== end:
        tree[node] = 1
        return
    change_tree(2*node,start,(start+end)//2,index)
    change_tree(2*node+1,(start+end)//2+1,end,index)
    tree[node] = tree[2*node] + tree[2*node+1]


input = sys.stdin.readline
n = int(input())
arr = [[int(input()),i] for i in range(n)]
arr.sort(key = lambda x: x[0])
for a in range(n):
    arr[a][0] = a
arr.sort(key= lambda x: x[1])
tree = [0]*(2**(math.ceil(math.log2(n))+1))
for i in range(n):
    change_tree(1,0,n-1,arr[i][0])
    print(i+1-find_sum(1,0,n-1,0,arr[i][0]-1))