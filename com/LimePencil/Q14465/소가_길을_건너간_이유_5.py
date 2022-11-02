import sys

input = lambda: sys.stdin.readline().rstrip()
n,k,b = list(map(int,input().split()))
broken=[0]*n
for _ in range(b):
    i = int(input())
    broken[i-1]=1
s=0
m=0
for i in range(n-k+1):
    if i==0:
        s=sum(broken[:k])
        m=s
    else:
        s-=broken[i-1]
        s+=broken[i+k-1]
        m=min(m,s)
print(m)