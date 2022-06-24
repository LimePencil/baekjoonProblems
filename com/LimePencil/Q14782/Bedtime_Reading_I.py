import sys

input = sys.stdin.readline
n = int(input())
s=0
for i in range(1,n+1):
    if n%i==0:
        s+=i
print(s)