import sys

input = sys.stdin.readline
n = int(input())
m=int(input())
s=n
for i in range(1,m+1):
    n*=10
    s+=n
print(s)