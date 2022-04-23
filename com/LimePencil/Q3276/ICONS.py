import sys
from math import ceil 

input = sys.stdin.readline
n = int(input())
minimum=float('inf')
x=1
y=1
for i in range(1,n):
    if minimum>i+ceil(n/i):
        minimum=i+ceil(n/i)
        x=i
        y=ceil(n/i)
print(x,y)