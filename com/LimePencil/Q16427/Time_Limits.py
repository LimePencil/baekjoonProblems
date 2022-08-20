from math import ceil
import sys

input = sys.stdin.readline
n,s = list(map(int,input().split()))
arr=list(map(int,input().split()))
for i in range(n):
    arr[i]=ceil(arr[i]*s/1000)
print(max(arr))