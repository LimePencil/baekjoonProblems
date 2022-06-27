import sys

input = sys.stdin.readline
x,y = list(map(int,input().split()))
n = int(input())
d=float('inf')
x1=0
y1=0
for _ in range(n):
    a,b = list(map(int,input().split()))
    if abs(x-a)+abs(y-b)<d:
        d=abs(x-a)+abs(y-b)
        x1=a
        y1=b
print(x1,y1)