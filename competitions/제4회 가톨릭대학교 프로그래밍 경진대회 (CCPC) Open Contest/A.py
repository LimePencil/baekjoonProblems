import sys

input = sys.stdin.readline
n,m=list(map(int,input().split()))
a,d= list(map(int,input().split()))
x,y=list(map(int,input().split()))
found=True
if d==0 and x==1 and y>a:
    found=False
elif d==1 and x==1 and y<a:
    found=False
elif d==0 and n==x and n%2==1:
    found=False
elif d==1 and n==x and n%2==0:
    found=False
print("YES!" if not found else "NO...")