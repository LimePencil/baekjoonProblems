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
n=int(input())
arr = [int(input()) for _ in range(n)]
arr_sorted = sorted(list(arr))
d = {arr_sorted[i] : i for i in range(n)}
tree = [0]*(n+1)
for i in range(n):
    print(query(d[arr[i]]+1))
    update(d[arr[i]]+1,1)