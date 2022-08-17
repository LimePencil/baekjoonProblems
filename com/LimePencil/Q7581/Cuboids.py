import sys

input = sys.stdin.readline
while True:
    a,b,c,d=list(map(int,input().split()))
    if a==b==c==d==0:
        break
    if a==0:
        print(d//(b*c),b,c,d)
    elif b==0:
        print(a,d//(a*c),c,d)
    elif c==0:
        print(a,b,d//(a*b),d)
    else:
        print(a,b,c,a*b*c)