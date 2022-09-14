import sys

input = sys.stdin.readline
n = int(input())
prev=1
for _ in range(n):
    a,b,c = input().split()
    a=int(a)
    c=int(c)
    if b=="+":
        prev=a+c-prev
    elif b=="-":
        prev=(a-c)*prev
    elif b=="*":
        prev=(a*c)**2
    else:
        prev=(a+1)//2
    print(prev)