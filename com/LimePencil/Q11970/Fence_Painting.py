import sys

input = sys.stdin.readline
a,b = list(map(int,input().split()))
c,d = list(map(int,input().split()))
fence=[0]*101
for i in range(a,b):
    fence[i]=1
for i in range(c,d):
    fence[i]=1
print(sum(fence))