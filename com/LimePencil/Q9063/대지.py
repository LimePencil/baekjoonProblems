import sys

input = sys.stdin.readline
x_s=[]
y_s=[]
for _ in range(int(input())):
    x,y=list(map(int,input().split()))
    x_s.append(x)
    y_s.append(y)
x_s.sort()
y_s.sort()
print((x_s[-1]-x_s[0])*(y_s[-1]-y_s[0]))