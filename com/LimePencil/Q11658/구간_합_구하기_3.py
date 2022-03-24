import sys

def update(x, y, val):
    while x <= n:
        tmp = y
        while tmp<=n:
            tree[x][tmp]+= val
            tmp+= (tmp&-tmp)
        x+=(x&-x)

def query(x, y):
    ans =0
    while x > 0:
        tmp = y
        while tmp > 0:
            ans += tree[x][tmp]
            tmp-= (tmp&-tmp)
        x-=(x&-x)
    return ans

input = sys.stdin.readline
n,m = list(map(int,input().split()))

tree = [[0]*(n+1) for _ in range(n+1)]
arr = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        update(i+1,j+1,arr[i][j])
for _ in range(m):
    l = list(map(int,input().split()))
    if l[0] == 0:
        w,x,y,c = l
        update(x,y,c-arr[x-1][y-1]) 
        arr[x-1][y-1] = c
    else:
        w,x1,y1,x2,y2 = l
        print(query(x2,y2)-query(x2,y1-1)-query(x1-1,y2)+query(x1-1,y1-1))