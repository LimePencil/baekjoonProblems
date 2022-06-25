import sys

input=sys.stdin.readline
s=int(input())
for _ in range(int(input())):
    a,b=map(int,input().split())
    s-=a*b
if s==0:
    print("Yes")
else:
    print("No")