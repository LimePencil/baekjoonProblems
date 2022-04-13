import sys

input = sys.stdin.readline
n,k = map(int,input().split(" "))
curr=0
for j in range(1,n+1):
    curr+=k-1
    curr%=j
    curr+=1
print(curr)