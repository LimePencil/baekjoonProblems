import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
l=[0]*n
for i in range(n):
    j=int(input())
    l[j-1]=i+1

print(*l,sep="\n")

