import sys

input = lambda: sys.stdin.readline().rstrip()
x1,y1,x2,y2 = list(map(int,input().split()))
x3,y3,x4,y4 = list(map(int,input().split()))
if x1>x4 or x2<x3 or y1<y4 or y2>y3:
    print(0)
    exit()
print(abs((max(x1,x3)-min(x2,x4))*(max(y2,y4)-min(y1,y3))))