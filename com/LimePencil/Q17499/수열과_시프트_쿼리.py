import sys

input = sys.stdin.readline
n,q=map(int,input().split())
arr=list(map(int,input().split()))
idx=0
for _ in range(q):
    order=list(map(int,input().split()))
    if order[0]==1:
        arr[(idx+order[1]-1)%n]+=order[2]
    elif order[0]==2:
        idx-=order[1]
        idx%=n
    else:
        idx+=order[1]
        idx%=n
    
print(*arr[idx:]+arr[:idx])