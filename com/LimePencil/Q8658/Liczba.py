import sys

input = sys.stdin.readline
n = int(input())
a=0
b=0
for i in range(2,n):
    if n%i!=0:
        a=i
        break
for i in range(n-1,1,-1):
    if n%i!=0:
        b=i
        break
print(a,b)