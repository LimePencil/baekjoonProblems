import sys

input = sys.stdin.readline
while True:
    a,b,c,d=list(map(int,input().split()))
    if a==0 and b==0 and c==0 and d==0:
        break
    if a>b:
        a,b=b,a
    if c>d:
        c,d=d,c
    print("{}%".format(min(100,min(c*100//a,d*100//b))))