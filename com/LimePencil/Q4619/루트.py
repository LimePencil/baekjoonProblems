import sys

input = sys.stdin.readline
while True:
    b,n=map(int,input().split())
    if b==0 and n==0:
        break
    a=int(b**(1/n))
    if abs(a**n-b)>abs((a+1)**n-b):
        print(a+1)
    else:
        print(a)