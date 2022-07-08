from math import lcm
import sys

ans=1
n=int(input())
arr=list(map(int,input().split()))
for i in range(n-2):
    ans=lcm(ans,arr[i])
print(ans)