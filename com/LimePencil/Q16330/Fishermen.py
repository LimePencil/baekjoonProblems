from bisect import bisect_left, bisect_right
import sys

def update(idx, val1,val2):
    while idx <= m:
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
n,m,d = list(map(int,input().split()))
limit=1000000000
fish = [list(map(int,input().split())) for _ in range(n)]
fisherman=list(map(int,input().split()))
sorted_fisherman=sorted(fisherman)
tree_one = [0]*(m+1)
tree_two = [0]*(m+1)
for i in range(n):
    a,b=fish[i]
    if b<=d:
        left= max(a-abs(b-d),1)
        right=min(a+abs(b-d),limit)
        l=bisect_left(sorted_fisherman,left)
        r=bisect_right(sorted_fisherman,right)-1
        range_update(l+1,r+1,1)
        pr=[]
        # for f in fisherman:
        #     a=bisect_left(sorted_fisherman,f)
        #     pr.append(query(a+1)-query(a))
        # print(*pr)
for f in fisherman:
    a=bisect_left(sorted_fisherman,f)
    print(query(a+1)-query(a))