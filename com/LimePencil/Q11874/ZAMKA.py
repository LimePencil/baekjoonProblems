import sys

input = sys.stdin.readline
l = int(input())
d = int(input())
x = int(input())
n=0
m=float('inf')
for i in range(l,d+1):
    s=sum(map(int,str(i)))
    if s==x:
        n=max(n,i)
        m=min(m,i)
print(m)
print(n)