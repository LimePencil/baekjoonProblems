import sys
from collections import defaultdict

input = sys.stdin.readline
n,s=map(int,input().split())
arr=list(map(int,input().split()))
half=n//2
other_half=n-half
count=0
sums=defaultdict(int)
for i in range(1<<half):
    poss=("{:0"+str(half)+"b}").format(i)
    add=0
    for j in range(half):
        if poss[j]=="1":
            add+=arr[j]
    sums[add]+=1
for i in range(1<<other_half):
    poss=("{:0"+str(other_half)+"b}").format(i)
    add=0
    for j in range(other_half):
        if poss[j]=="1":
            add+=arr[j+half]
    if s-add in sums:
        count+=sums[s-add]
print(count if s!=0 else count-1)