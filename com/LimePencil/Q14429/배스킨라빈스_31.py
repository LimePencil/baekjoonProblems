import sys

input = sys.stdin.readline
n = int(input())
minimum = float('inf')
index = 0
for i in range(1,n+1):
    n,m = list(map(int,input().split(" ")))
    v = ((n-1)//(m+1)+1)*2
    if minimum>v:
        minimum = v
        index = i
print(index,minimum)