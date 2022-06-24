import sys

input = sys.stdin.readline
while True:
    a,b,c = list(map(int,input().split()))
    if a==b==c==0:
        break
    
    if a==0:
        a=c//b
    elif b==0:
        b=c//a
    else:
        c=a*b
    print(a,b,c)