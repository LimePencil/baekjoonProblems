import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    x1,y1,z1,x2,y2,z2 = list(map(int,input().split()))
    print(abs(x1-x2)+abs(y1-y2)+z1+z2)