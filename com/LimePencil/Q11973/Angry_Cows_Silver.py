import sys

def num_cow_needed(r):
    index_covered=-1
    cow_cnt=0
    for h in hays:
        if h>index_covered:
            cow_cnt+=1
            index_covered=2*r+h
    return cow_cnt

input = lambda: sys.stdin.readline().rstrip()
n,k = list(map(int,input().split()))
hays = sorted([int(input()) for _ in range(n)])

l=0
r=1000000000

while l<=r:
    m=(l+r)//2
    if num_cow_needed(m)<=k:
        r=m-1
    else:
        l=m+1
print(l)