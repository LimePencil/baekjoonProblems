from math import ceil
import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr = list(map(int,input().split()))
b,c=list(map(int,input().split()))
cnt=0
for num in arr:
    num-=b
    cnt+=1+max(0,ceil(num/c))
print(cnt)