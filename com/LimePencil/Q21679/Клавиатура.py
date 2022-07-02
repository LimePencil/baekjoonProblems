import sys

input = sys.stdin.readline
n = int(input())
key = list(map(int,input().split()))
m = int(input())
type = list(map(int,input().split()))
for i in range(m):
    key[type[i]-1]-=1
for i in range(n):
    if key[i]<0:
        print("yes")
    else:
        print("no")