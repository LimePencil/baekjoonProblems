import sys

input = sys.stdin.readline
n,x,k = list(map(int,input().split()))
for _ in range(k):
    a,b=list(map(int,input().split()))
    if a==x:
        x=b
    elif b==x:
        x=a
print(x)