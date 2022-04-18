import sys
from collections import defaultdict

input = sys.stdin.readline
n,m=map(int,input().split())
arr = list(map(int,input().split()))
count=defaultdict(int)
previous_prefix_sum=0
ans=0
for i in range(n):
    previous_prefix_sum=(previous_prefix_sum+arr[i])%m
    count[previous_prefix_sum]+=1
for i in range(m):
    ans+=(count[i]*(count[i]-1))//2
print(ans+count[0])